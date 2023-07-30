import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect powdery mildew leaves have clear marks/signs; "
        f"typically, the leaves are light roughly-circular, powders-looking"
        f"patches on young, susceptible leaves (light green expanding leaves)"
        f" that can differentiate from healthy leaves. \n\n"
        f"* An Image Montage shows that typically powdery mildew leaves have"
        f"fine white powdery marks across. "
        f"Average Image, Variability Image, and Difference between Averages"
        f"studies didn't reveal "
        f"any clear pattern to differentiate one from another."
    )
