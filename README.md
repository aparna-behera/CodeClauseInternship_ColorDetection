## Python Project on Color Detection using OpenCv

Color detection is the process of detecting the name of any color.
In this project, we are building an application using Python's OpenCV library, through which you can automatically get the name of the color by clicking on them. 

## Contents

This repository contains:

- **colors.csv**: A data file that contains 865 color names along with their RGB and hex values. We need to calculate the distance from each color and find the shortest one.
- **colorpic.jpg, test_image1.jpg**: Sample images to check if the code is working as expected.
- **project_color_detection.py**: Main source code of the project.

## Approach

Step 1: Load the input image. I have used the sample image 'colorpic.jpg'.
Step 2: Resize the image to maintain a standard size for all the input images.
Step 3: Load the 'colors.csv' dataset using pandas library.
Step 4: Implement a function 'get_color' to calculate the minimum distance between the color from the image and all the colors in the 'colors.csv' dataset and get the most matching color.
Step 5: Implement a callback function 'display_color' to capture the Mouse Event and display the corresponding color name on the image. The 'display_color' function is called everytime a mouse event occurs (which is double click in this case).
