import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


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
        st.success(prediction)


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

    # img=Image.open('./upload_image.jpg')
    # new_img=img.resize((300,300))
    


    img=st.file_uploader("Choose an image",type=['jpg','png','.jpeg'])
    st.button("Predict",key=1,on_click=predict(img))


    captured_img=st.camera_input("Click a pic")
    st.button("Predict",key=2,on_click=predict(captured_img))
    

    

if __name__=='__main__':
    main()
