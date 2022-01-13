import streamlit as st
import cv2
import numpy as np


def show():

    def preprocess(img):
        bytes_data = np.asarray(bytearray(img.read()), dtype=np.uint8)
        img = cv2.imdecode(bytes_data, cv2.IMREAD_COLOR)
        return img

    def invert(img):
        img = preprocess(img)
        inv = cv2.bitwise_not(img)
        return inv

    def hdr(img):
        img = preprocess(img)
        hdr_img = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
        return  hdr_img

    def sketch(img):
        img = preprocess(img)
        _, sketch_img = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
        return  sketch_img

    def gray(img):
        img = preprocess(img)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_img=cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
        return gray_img

    def none(img):
        img = preprocess(img)
        return img

    picture = st.camera_input("First, take a picture...")

    filters_to_funcs = {
        "No filter": none,
        "Invert": invert,
        "HDR": hdr,
        "Sketch": sketch,
        "Grayscale": gray
    }
    filters = st.selectbox("...and now, apply a filter!", filters_to_funcs.keys())
    
    if picture:
        st.image(filters_to_funcs(filters)(picture), channels="BGR")
