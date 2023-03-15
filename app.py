import streamlit as st
import tensorflow as tf
# from tensorflow import keras
# from tf.keras.utils import img_to_array
# from tensorlfow.keras.models import load_model
import numpy as np
from PIL import Image

result=""
classes=['1-1','1-2','1-4','PURE']

def predict(img):
    model=tf.keras.models.load_model('./My_CNN_Model.h5')
    if img is not None:
        st.image(img)
        x_=Image.open(img)
        x_=x_.resize((256,256))
        x=tf.keras.utils.img_to_array(x_)
        x=x/255
        processed_img=np.expand_dims(x,axis=0)
        pred=model.predict(processed_img)
        prediction=classes[np.argmax(pred)]
        st.write(prediction)


def getPic():
    st.camera_input("Click a Pic")




def main():
    title="""
    <h2 style='text-align: center'>
    Find Adulteration in Turmeric Powder
    </h2>
    """
    st.markdown(title,unsafe_allow_html=True)
    # img=Image.open('./upload_image.jpg')
    # new_img=img.resize((300,300))
    # st.image(new_img)
    # column1,column2,column3=st.columns([2,1,2])
    # column1.button("Upload an Image",use_container_width=True)
    # # column2.button()
    # column3.button("Click a Picture",use_container_width=True)
    img=st.file_uploader("Choose an image",type=['jpg','png','.jpeg'])
    st.button("Predict",on_click=predict(img))
    

if __name__=='__main__':
    main()
