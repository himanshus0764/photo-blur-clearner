import cv2
import numpy as np
import configparser
import tkinter as tk
from tkinter import filedialog

def load_config(config_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_path)
    image_path = config.get('Settings', 'image_path', fallback='')
    return image_path

def save_config(image_path, config_path='config.ini'):
    config = configparser.ConfigParser()
    config['Settings'] = {'image_path': image_path}
    with open(config_path, 'w') as config_file:
        config.write(config_file)

def get_image_path_from_user():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select Image")
    return file_path

def deblur_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Unable to read the image at path {image_path}")
        return
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a blur to simulate the original blur (you might skip this if you already have a blurry image)
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    
    # Use Wiener deconvolution for deblurring
    psf = np.ones((5, 5), np.float64) / 25  # Point Spread Function (PSF)
    deblurred = cv2.filter2D(blurred, -1, psf)
    
    # Save the deblurred image
    cv2.imwrite('deblurred_image.jpg', deblurred)
    print("Deblurred image saved as 'deblurred_image.jpg'")
    
    # Display the original, blurred, and deblurred images
    cv2.imshow('Original', gray)
    cv2.imshow('Blurred', blurred)
    cv2.imshow('Deblurred', deblurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Prompt user to select a file using a file dialog
user_file_path = get_image_path_from_user()

if user_file_path:
    # Check if the selected file is an image (you can add more image extensions if needed)
    image_extensions = ['.jpg', '.jpeg', '.png']
    if any(user_file_path.lower().endswith(ext) for ext in image_extensions):
        # Process the image and save the deblurred image
        deblur_image(user_file_path)
        
        # Save the updated image path to the config file
        save_config(user_file_path)
    else:
        print("Selected file is not a supported image format. Exiting.")
else:
    print("No file selected. Exiting.")
