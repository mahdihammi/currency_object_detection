# Tunisian Banknotes Object Detection
This project focuses on detecting and identifying Tunisian banknotes using object detection techniques. It utilizes Python, YOLOv5 for object detection, Labelimg for data annotation, and Streamlit for creating a web interface.

I worked on this projects in google colab, so the paths in dataset.yml and the folders of train val test were presented in my drive. <br>

# Project Overview
The objective of this project is to create a reliable system to detect and identify different denominations of Tunisian banknotes. This system can be used in various applications, such as automated teller machines (ATMs), vending machines, and other financial technologies requiring currency recognition.

# Dataset Preparation
Image Collection: Images of various denominations of Tunisian banknotes were collected from different sources.
Data Augmentation: Techniques such as rotation, flipping, and scaling were applied to increase the size and diversity of the dataset and improve the robustness of the model.

## Annotation: The images were annotated using Labelimg, saving the annotations in YOLO format.
Dataset Organization: The dataset was organized into images and labels folders.
Data Split: The dataset was split into training, validation, and test sets.

# Model Training
Downloading YOLOv5: The YOLOv5 repository was cloned and set up for training.
Custom Dataset Preparation: The annotated images and labels were placed in the appropriate directories by creating a .yaml file to define the dataset structure. The .yaml file should specify the paths to the training, validation, and test datasets, as well as the names of the classes.
Training: The YOLOv5 model was trained on the prepared dataset with specified parameters to optimize performance.
Model Export: After training, the best model was exported for inference.

# Web Application
Streamlit Setup: Developed a Streamlit application to provide a user-friendly interface for banknote detection.
You can see The User Interface in streamlit :

![appaa](https://github.com/mahdihammi/currency_object_detection/assets/89527502/55731765-a31b-48d4-be6f-2ed398088082)

# Challenges
Computer Resources: During the development of this project, I encountered a significant challenge related to the limitations of my computer resources. Specifically, the real-time detection feature often failed and experienced substantial lag.


# Here are Some of the results of the inference : <br>
![10dt](https://github.com/mahdihammi/currency_object_detection/assets/89527502/4f713409-b47e-4c86-b976-1a8ac931d4dc)
![test_img_33](https://github.com/mahdihammi/currency_object_detection/assets/89527502/5d5769d5-8475-4332-b51d-42ca8d2f0a68)
![10dtall](https://github.com/mahdihammi/currency_object_detection/assets/89527502/aead301e-3c2c-4db3-8e77-d1a7d0ca036a)
![10_20_2](https://github.com/mahdihammi/currency_object_detection/assets/89527502/99a6e1b4-f99c-4fe2-9990-4e06dcd4604b)
