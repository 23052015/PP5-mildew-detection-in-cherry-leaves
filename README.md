
# Mildew Detection in Cherry Leaves

---

The created app is a powerful application that can accurately predict whether cherry leaves are healthy or infected with powdery mildew. By analyzing an image of a cherry leaf, the app employs a sophisticated machine learning model for supervised, single-label, binary classification. Through this binary classifier, the app determines whether the leaf is healthy or afflicted with the disease, providing users with valuable insights into the condition of their cherry trees.

- [Mildew Detection in Cherry Leaves](#mildew-detection-in-cherry-leaves)
  - [Cloud IDE Reminders](#cloud-ide-reminders)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Hypothesis and how to validate?](#hypothesis-and-how-to-validate)
  - [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
    - [Business Requirement 1](#business-requirement-1)
    - [Business Requirement 2](#business-requirement-2)
  - [ML Business Case](#ml-business-case)
  - [Dashboard Design](#dashboard-design)
  - [Fixed Bugs](#fixed-bugs)
  - [Deployment](#deployment)
  - [Steps to run the browser in the workspace using codeanywhere](#steps-to-run-the-browser-in-the-workspace-using-codeanywhere)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Future improvements to increase the app potential](#future-improvements-to-increase-the-app-potential)

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with *Regenerate API Key*.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.

- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a      fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

- Our observations indicate that powdery mildew leaves exhibit distinct marks and signs. Typically, these marks manifest as light, roughly-circular, powdery patches on young and susceptible leaves with light green expanding foliage, making them distinguishable from healthy leaves.
- Upon analyzing the Image Montage, it is evident that powdery mildew leaves commonly feature fine white marks throughout their surface. However, when studying the Average Image, Variability Image, and Difference between Averages, we did not find any definitive pattern that could be used to differentiate one from another.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requirement 1

As a client, I require the ability to visualize "mean" and "standard deviation" images for both healthy cherry leaves and cherry leaves containing powdery mildew. This visualization will allow me to easily differentiate between the two types of cherry leaves. Additionally, I need to view the differences between an average healthy cherry leaf and an average cherry leaf with powdery mildew, aiding me in visually distinguishing between them. Lastly, I would like to have an image montage showcasing healthy cherry leaves and those with powdery mildew, further facilitating visual differentiation.

### Business Requirement 2

As a client, I seek a predictive capability that can determine whether a given cherry leaf is healthy or affected by powdery mildew. To achieve this, I require the development of a robust machine learning (ML) model capable of generating accurate predictions. Furthermore, I need the ML model to generate comprehensive reports, providing valuable insights and analysis regarding the classification results.

## ML Business Case

1. Business Objective: Our primary goal is to develop a method/tool that enhances the accuracy and efficiency of evaluating cherry leaves infected with powdery mildew compared to healthy leaves.
2. Customer Dashboard: The customer seeks a user-friendly dashboard with image upload functionality. The dashboard will leverage machine learning to rapidly determine if a leaf image represents a healthy leaf or one infected with powdery mildew, achieving an impressive accuracy of 97%.
3. Data Privacy: The customer emphasizes the need for strict data privacy to safeguard their proprietary information. To prevent competitors from replicating their cherry leaf production, internal data will remain confidential and undisclosed.
4. ML Model Training: The ML tool will be trained using input images of both healthy and infected cherry leaves. Its objective is to discern the distinctions between the two types of leaves effectively. The desired outcome is an ML model with 97% accuracy, capable of determining if an uploaded leaf image is healthy or infected.
5. Conventional Data Analysis: In addition to the ML-based approach, conventional data analysis techniques can also be employed to visually inspect and differentiate leaf images, aiding in the identification of healthy and powdery mildew-infected leaves.

## Dashboard Design

The app is separated in 5 large sections

1. Quick project summary
   On this page we can find general information about the roject, the dataset summary and the business requirements.
![Project Summary](https://github.com/23052015/PP5-mildew-detection-in-cherry-leaves/assets/109954194/71918cf2-ef14-455a-a835-8e01e8bed22e)

2. Cherry Leaf Visualizer

**Business requirement 1**

![Cherrry Leaves Visualizer ](https://github.com/23052015/PP5-mildew-detection-in-cherry-leaves/assets/109954194/4a50002e-3a9f-46bb-adbb-a3e103de522e)

- This page visualizes the difference between:
     healthy average/variable and infected average/variable
![Difference btw average healthy and average infected](https://github.com/23052015/PP5-mildew-detection-in-cherry-leaves/assets/109954194/46e21efd-f573-432a-9ca2-cd27f32cedaf)

- Image Montage(healthy)
![Image montage (healthy)](https://github.com/23052015/PP5-mildew-detection-in-cherry-leaves/assets/109954194/bb656a2f-1864-4ea5-a747-ce65d1b66aec)

- Image Montage(infected)
![Image montage powdery mildew](https://github.com/23052015/PP5-mildew-detection-in-cherry-leaves/assets/109954194/83269313-42c7-4d8b-8d01-ae94384a8192)

3. Mildew Detector

**Business Requirement 2**

  The application must include the following features:

- Link to Download Images: Users should be able to download a collection of images containing both healthy and unhealthy leaves. These images will be used for live predictions.* User Interface with File Uploader: The application should have a user-friendly interface with a file uploader widget. Users can upload images of leaves, and the uploaded image will be displayed along with a prediction statement indicating whether the leaf is healthy or unhealthy.
- Prediction Table: A table will be provided that lists the names of the uploaded images along with the corresponding prediction results (healthy or unhealthy).
- Download Button for Table: The application should have a download button that allows users to download the prediction table for future reference or analysis.
![Analysis healthy 1](https://github.com/23052015/PP5-mildew-detection-in-cherry-leaves/assets/109954194/cae0f5b2-4c96-4a9f-84b0-23853d981ad2)
![Analysis healthy 2](https://github.com/23052015/PP5-mildew-detection-in-cherry-leaves/assets/109954194/1a97f79f-0e7a-42ba-9be6-d191ddba8cb7)
![Analysis infected 1](https://github.com/23052015/PP5-mildew-detection-in-cherry-leaves/assets/109954194/d8e4e444-2ac5-4f31-9d98-08239724c2e7)
![Analysis infected 2](https://github.com/23052015/PP5-mildew-detection-in-cherry-leaves/assets/109954194/26e7fcc6-1aec-40e8-a78f-2fdd8de3d8a0)

4. Project hypothesis
   This page shows the project hypothesis and how it is validated across the project
![Project hypothesis](https://github.com/23052015/PP5-mildew-detection-in-cherry-leaves/assets/109954194/4e859979-c32f-442d-aac2-dfc16414d6da)

5. Model performance metrics
   This page shows the technical part of the model performance. The bar graph illustrates the distribution of images across different labels in the train, validate, and test datasets. The line    graphs depict a normal learning curve by displaying accuracy and loss plots. Additionally, the last table provides a tabular representation of the same information. The machine learning        model exhibits excellent performance with a remarkable accuracy of 99%.

## Fixed Bugs

- When the app was deployed it was originally a fail due to the fact that the stack does not support the used python version. This was fixed ba setting the stack of    the project through codeanywhere workspace from 22 to 20.

## Deployment

**Heroku**

- The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Steps to run the browser in the workspace using codeanywhere

- Open the codeanywhere Workspace

- Open a new terminal
- Write in the terminal "streamlit run app.py" and a port will open which would show the code in the browser

## Main Data Analysis and Machine Learning Libraries

- Numpy: aA powerful library used to handle multi-dimensional arrays and offers an extensive collection of mathematical functions to perform operations on these arrays efficiently.

- Pandas: A valuable tool for data analysis, facilitating statistical analysis and manipulation of datasets.
- Matplotlib: Primarily used for data visualization and enables the embedding of plots within Jupyter notebooks.
- Seaborn: Provides a high-level interface for creating statistical graphics, offering built-in themes to style Matplotlib plots elegantly.
- Plotly: Well-suited for plotting data, adding interactivity and animation to data visualizations.
- Scikit-learn: Contains a comprehensive suite of tools for predictive analysis, enabling the training of machine learning models for classification and clustering tasks.
- TensorFlow: A popular library utilized to iteratively optimize models during training by employing an optimizer and loss function.
- Keras: Serves as a user-friendly Python interface for building artificial neural networks.
- Itertools: valuable for efficiently iterating over data structures that can be traversed using a for-loop.
- Random: Commonly used to generate random numbers, which is often necessary for various algorithms and simulations.

## Credits

- [Code Institute Malaria Walkthrough Project](https://github.com/Code-Institute-Solutions/WalkthroughProject01) was extensively used to create this project.
  The complete design and almost the complete code has been taken from Malaria Walkthrough Project.
- [Mildew Detection in Cherry leaves MilestonePP5](https://github.com/ssreelakshmi88/mildew-detection-cherry-leaves_milestonePP5) was a great help in order to get see how a succesfull implementation of this project looks like.
- [Mildew Detection Project](https://github.com/Erik1007/mildew-detection-project) was also used as a reference for this project.
- Code Institute Student support was very kind for granting 1 day extension of the deadline for this project.
- Slack community and especially Niel McEwen for his support in troubleshooting.
- I want to express my gratitude towards my Mentor Rohit Sharma for his support and guideness throughout this project.

### Content

- Minor parts about the powdery mildew disease have been taken from
  [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew)
- Other parts are well known by myself since I have a wineyard which (depends
  on the season) faces this problem.

### Media

- The cherry leaves images dataset was taken from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)

## Future improvements to increase the app potential

- Since I have my own wineyard and know that humid and rainy weather increase the chance of infection by powdery mildew, the app could be upgraded
  in that way that sensors which measure humidity are placed in the area where cherry trees are placed and connected with the app to issue
  warnings about increased possibility of infection by powdery mildew so that the client could react properly by treating the trees with fungicides or/and
  implement other measures (sanitation, pruning etc.).
  
- A leaf scanner/camera mounted on a vehicle and connected with the app (for example tractor/low flying drone) which could scan large amount of trees in a short period of time.
