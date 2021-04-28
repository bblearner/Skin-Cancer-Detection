import numpy as np
import tensorflow as tf
import streamlit as st
from PIL import Image, ImageOps
#from image_classification import teachable_machine_classification

def teachable_machine_classification(img, weights_file):
    #load the model
    model = tf.keras.models.load_model(weights_file)

    #create the array of the rigth shape to feed into the keras model
    image = img
    #image sizing
    size = (256,256)
    image = ImageOps.fit(img, size, Image.ANTIALIAS)

    #turn the image into numpy array 
    image_array = np.asarray(image)

    #run the inference
    prediction = model.predict(np.expand_dims(image_array, axis=0))
    class_names = ['melanoma', 'nevus', 'seborrheic_keratosis']
    return class_names[np.argmax(prediction)]


st.title("Image Classification with Google's Teachable Machine")
st.header("Skin Cancer Prediction")

uploaded_file = st.file_uploader("Upload the skin lesion image ...", type='jpg')
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    class_name = teachable_machine_classification(image, 'cancer_prediction')
    st.write(f"You seem to have {class_name}")
    if class_name == 'melanoma':
        st.write("You should consult a medical practinioner.")
    else:
        st.write("You should be safe but should still consult a medical practinioner.")