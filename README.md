## Python Project on Color Detection using OpenCV

Color detection is the process of detecting the name of any color.
In this project, we are building an application using Python's OpenCV library, through which you can automatically get the name of the color by clicking on them. 

## Contents

This repository contains:

- **colors.csv**: A data file that contains 865 color names along with their RGB and hex values. We need to calculate the distance from each color and find the shortest one.
- **colorpic.jpg, test_image1.jpg**: Sample images to check if the code is working as expected.
- **project_color_detection.py**: Main source code of the project.

## Approach

- Step 1: Load the input image. I have used the sample image "colorpic.jpg".
- Step 2: Resize the image to maintain a standard size for all the input images.
- Step 3: Load the "colors.csv" dataset using pandas library.
- Step 4: Implement a function "get_color()" to calculate the minimum distance between the color in the image and all the colors in the 'colors.csv' dataset and return the most matching color.
- Step 5: Set the cv2.MouseCallback function that calls "display_color()" whenever a mouse event occurs.
- Step 6: By double clicking on any color in the image, its name is displayed on the image with the help of "display_color()" function.
