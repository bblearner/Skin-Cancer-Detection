# Skin-Cancer-Detection
Detecting Melanoma skin lesion using CNN

The colab notebook can be found at here https://colab.research.google.com/drive/1-h2whMrHFf5dA7BJbKq4zAOKCLiGJjjX?usp=sharing

This is a CNN Model for classifying between nevi, seborrheic keratoses and melanoma(which is the deadliest form of skin cancer). 
I used the **tensorflow** and **scikit-learn** library for model building and data preparation also I made a basic application for running the model using the **streamlit** library whose code is provided in the app.py file. 
To run the application simply load the model from the drive link and run in the terminal 'Streamlit run app.py'.
The trained model weights can be found on this link https://drive.google.com/drive/folders/15dUuGuQYv_5IoslN39BYy5aotO2-WL-a?usp=sharing.

The data and objective are pulled from the 2017 ISIC Challenge on Skin Lesion Analysis Towards Melanoma Detection. 

The dataset can be found here https://s3-us-west-1.amazonaws.com/udacity-dlnfd/datasets/skin-cancer/train.zip(5.3 GB), https://s3-us-west-1.amazonaws.com/udacity-dlnfd/datasets/skin-cancer/valid.zip(824.5 GB), https://s3-us-west-1.amazonaws.com/udacity-dlnfd/datasets/skin-cancer/test.zip (5.1 GB). 

The final model achieves 80% percent accuracy on the testing dataset. This short paper was used as a reference for the model https://arxiv.org/ftp/arxiv/papers/1703/1703.03108.pdf.

The colab notebook for the project can be found here https://colab.research.google.com/drive/1-h2whMrHFf5dA7BJbKq4zAOKCLiGJjjX?usp=sharing
