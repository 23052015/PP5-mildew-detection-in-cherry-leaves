import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random


def page_leaves_visualizer_body():
    """
    Displays the leaves visualizer page
    """

    st.header("Cherry leaves Visualizer")

    st.success(
        f"This page will provide a visual reference of the difference between "
        f"a **healthy** Cherry Leaf and a Cherry Leaf infected with "
        f" **powdery mildew**. \n\n"
    )

    version = 'v1'
    displays_avg_var_images(version)
    display_diff_between_avg_images(version)
    display_image_montage()


def displays_avg_var_images(version):
    """
    Displays the average and variability images
    """

    st.subheader("Difference between average and variablity images")

    avg_var_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
    avg_var_powdery_mildew = plt.imread(
        f"outputs/{version}/avg_var_powdery_mildew.png")

    st.success(
        f"After careful observation, we have identified a significant visual"
        f" difference in consistent coloring between healthy and infected"
        f" leaves. The average and variability images of infected leaves"
        f" exhibit more prominent white color blotches on their surface"
        f" compared to healthy leaves, which are characterized by a greenish"
        f" uniform coloring. However, it is worth noting that the average and"
        f" variability images did not reveal any clear patterns that could"
        f" intuitively differentiate infected leaves from healthy leaves."
    )

    st.image(avg_var_healthy, caption='Healthy leaves-average and variable')
    st.image(avg_var_powdery_mildew,
             caption='Powdery Mildew infected-average and variable')
    st.write("---")


def display_diff_between_avg_images(version):
    """
    Displays the difference between average healthy
    and average infected image
    """
    st.subheader(f"Difference between average healthy"
                 f" and average infected leaves")

    diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

    st.success(f"We observe a similar pattern here, where the healthy leaves"
               f" have a clearer, green surface, and the infected ones display"
               f" more white color on the surface."
               f" However, comparing both kinds of leaves remains challenging."
               )

    st.image(diff_between_avgs, caption="Difference between average images")


def display_image_montage():
    """
    Displays image montage
    """

    st.subheader("Image Montage")
    st.write("* To create & refresh the montage, click on 'Create Montage'")
    st.info(
        f"* The montage helps visually differentiate between healthy and "
        f" infected leaf. The infected leaf has white, powdery spots or "
        f" patches on the top side of leaves"
    )

    my_data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
    labels = os.listdir(my_data_dir + '/validation')
    label_to_display = st.selectbox(
        label="Select label:", options=labels, index=0
    )

    if st.button("Create Montage"):
        image_montage(dir_path=my_data_dir + '/validation',
                      label_to_display=label_to_display,
                      nrows=8, ncols=3, figsize=(10, 25))

    st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    """
    This function creates and displays image montage
    """

    sns.set_style("ticks")
    labels = os.listdir(dir_path)

    images_list = os.listdir(dir_path + '/' + label_to_display)
    if nrows * ncols < len(images_list):
        img_idx = random.sample(images_list, nrows * ncols)
    else:
        print(
            f"Decrease nrows or ncols to create your montage.\n"
            f"There are{len(images_list)} in your subset. "
            f"You requested a montage with {nrows * ncols} spaces"
        )
        return

    list_rows = range(0, nrows)
    list_cols = range(0, ncols)
    plot_idx = list(itertools.product(list_rows, list_cols))

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    for i in range(0, nrows*ncols):
        img = imread(f"{dir_path}/{label_to_display}/{img_idx[i]}")
        img_shape = img.shape
        axes[plot_idx[i][0], plot_idx[i][1]].imshow(img)
        axes[plot_idx[i][0], plot_idx[i][1]].set_title(
            f"Width {img_shape[1]}px x Height {img_shape[0]}px")
        axes[plot_idx[i][0], plot_idx[i][1]].set_xticks([])
        axes[plot_idx[i][0], plot_idx[i][1]].set_yticks([])
    plt.tight_layout()

    st.pyplot(fig=fig)


# Run the app
if __name__ == "__main__":
    page_leaves_visualizer_body()
