import streamlit as st
import os
import subprocess
import time
import glob

st.title("Tunisian Dinar Bill Detection")
icon_url = "./tounes.png"
st.image(icon_url, width=50)

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])



# Button to start detection
if uploaded_file is not None:
        # Save the uploaded image to a temporary location
        image_path = uploaded_file.name
        
        # Run YOLOv5 detection using the uploaded image as the source and i used the detec.py file
        cmd = f"cd C:/Users/Mahdi/Desktop/workspase/Projects/currencyOD/app/yolov5 && python detect.py --source {image_path} --weights C:/Users/Mahdi/Desktop/workspase/Projects/currencyOD/app/yolov5/best.pt --img-size 320 --conf 0.4"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()
        # ploting the result of the last exp :)
       

                # Function to find the last subfolder within a directory
        def find_last_subfolder(directory):
            subfolders = [f for f in glob.glob(os.path.join(directory, '*')) if os.path.isdir(f)]
            if not subfolders:
                return None
            return max(subfolders, key=os.path.getmtime)

        detect_folder = "./yolov5/runs/detect"
        last_subfolder = find_last_subfolder(detect_folder)

        # Check if a last subfolder was found
        if last_subfolder is None:
            st.warning("No subfolders found within the 'detect' folder.")
        else:
            # Get image
            image_files = [f for f in glob.glob(os.path.join(last_subfolder, '*.jpg'))] + [f for f in glob.glob(os.path.join(last_subfolder, '*.png'))]

            if not image_files:
                st.warning("No image files found in the last subfolder.")
            else:
                # Select the latest image file from the last subfolder
                latest_image = max(image_files, key=os.path.getmtime)
                st.image(image_path, use_column_width=True)
                st.image(latest_image, use_column_width=True)
        
