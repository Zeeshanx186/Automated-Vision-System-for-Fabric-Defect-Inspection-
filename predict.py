from ultralytics import YOLO
import cv2
import streamlit as st
from PIL import Image

import numpy as np

modelpath = r"best_1.pt"
model = YOLO(modelpath)

st.title('Predict Fabrics Defects')

# Function to capture image from camera
def capture_frame():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cap.release()
    return ret, frame

# Function to perform prediction
def predict_defect(image):
    results = model(image)
    if results:
        print("Defect in Image")
        return results  # Return the results
    else:
        print("No defect Detected")
        return []  # Return an empty list

# Main Streamlit app
def main():
    st.sidebar.title('Options')
    use_camera = st.sidebar.checkbox('Use Camera', True)
    capture_video = st.sidebar.checkbox('Capture Video', False)

    if use_camera:
        st.subheader('Live Camera Feed')
        capture_button = st.button("Capture Image")
        if capture_button:
            ret, frame = capture_frame()
            if ret:
                st.image(image=frame, channels='RGB')
                results = predict_defect(frame)
                if len(results[0].boxes) > 0:
                    st.write("Defect in Image")
                else:
                    st.write("No defect Detected")

    if capture_video:
        st.subheader('Live Video Feed')
        while True:
            frame = capture_frame()
            if frame[0]:
                st.image(image=frame[1], channels='RGB')
                results = predict_defect(frame[1])
                if len(results[0].boxes) > 0:
                    st.write("Defect in Image")
                else:
                    st.write("No defect Detected")
            else:
                st.write('Error: Unable to capture frame from the camera.')
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    st.sidebar.markdown('---')

    st.sidebar.subheader('Upload Image')
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        results = predict_defect(image)
        if len(results[0].boxes) > 0:
            st.write("Defect in Image")
        else:
            st.write("No defect Detected")

if __name__ == "__main__":
    main()
