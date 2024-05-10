# photo-blur-clearner
The Photo Blur Clearer utilizes a combination of image deblurring algorithms and enhancement filters to address various types of blur, including motion blur, out-of-focus blur, and Gaussian blur. By analyzing the characteristics of the blur and applying appropriate processing techniques, the tool aims to restore sharpness and detail to the image,
# Image Deblurring Script

The Image Deblurring Script is a Python script designed to deblur images using the Wiener deconvolution method. Leveraging the OpenCV library for image processing and Tkinter for the user interface, this script provides a convenient way to deblur images and visualize the deblurring process.

## Description

The Image Deblurring Script utilizes the Wiener deconvolution method to restore clarity and sharpness to blurred images. By simulating the original blur and applying appropriate deblurring techniques, the script aims to enhance the quality of input images, resulting in clearer and more visually appealing results.

## Features

- **File Selection**: Users can select an image file using a file dialog, enabling seamless integration with existing image files and directories.
- **Image Deblurring**: The script applies the Wiener deconvolution method to deblur the selected image, restoring detail and sharpness to the image.
- **Visualize Results**: The script displays the original image, blurred image, and deblurred image side by side, allowing users to visualize the deblurring process and compare the results.

## Usage

1. **Select Image**: Run the script and select an image file using the file dialog.
   
2. **Deblur Image**: The script will apply the Wiener deconvolution method to deblur the selected image, generating a deblurred version of the image.
   
3. **Visualize Results**: The script will display the original image, blurred image, and deblurred image side by side for comparison and analysis.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`) library
- NumPy (`numpy`) library
- Tkinter (`tkinter`) library (usually included with Python installations)

## Note

- The Image Deblurring Script is designed to enhance the clarity and sharpness of blurred images using the Wiener deconvolution method. While it can effectively deblur many types of images, it may not fully restore images with severe degradation or distortion.

## Author

[Himanshu sharma]
