import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


classes=['1-1','1-2','1-4','PURE']

def predictCapturedImage(img):
    model=tf.keras.models.load_model('./My_CNN_Model.h5')
    if img is not None:
        x_=Image.open(img)
        x_=x_.resize((256,256))
        x=tf.keras.utils.img_to_array(x_)
        x=x/255
        processed_img=np.expand_dims(x,axis=0)
        pred=model.predict(processed_img)
        prediction=classes[np.argmax(pred)]
        return prediction
    else:
        return ""


def predictUploadedImage(img):
    model=tf.keras.models.load_model('./My_CNN_Model.h5')
    if img is not None:
        column1,column2,column3=st.columns([0.1,1,0.1])
        column1.write(" ")
        column2.image(img)
        column3.write(" ")
        x_=Image.open(img)
        x_=x_.resize((256,256))
        x=tf.keras.utils.img_to_array(x_)
        x=x/255
        processed_img=np.expand_dims(x,axis=0)
        pred=model.predict(processed_img)
        prediction=classes[np.argmax(pred)]
        return prediction
    else:
        return ""


def main():
    handle_style = """
        <style>
        #MainMenu {visibility: hidden;}

        .block-container
        {
            padding-top: 1rem;
            padding-bottom: 3rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        </style>
        """
    st.markdown(handle_style, unsafe_allow_html=True)

    title="""
    <h3 style="text-align: center;">
        Find Adulteration in Turmeric Powder
    </h3>
    """
    st.markdown(title,unsafe_allow_html=True)


    captured_img=st.camera_input("Click a picture")
    result1=predictCapturedImage(captured_img)
    
    img=st.file_uploader("Choose an image file",type=['jpg','png','.jpeg'])
    result2=predictUploadedImage(img)

    if (result1=="" and result2==""):
        st.success("Please capture or select one image to predict adulreration")
    elif (result1!="" and result2==""):
        st.success(result1)
    elif (result2!="" and result1==""):
        st.success(result2)
    else:
        st.success(result1)
        st.success(result2)



    

    

if __name__=='__main__':
    main()
