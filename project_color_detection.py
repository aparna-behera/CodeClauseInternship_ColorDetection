# Importing the libraries

import cv2
import pandas as pd


# Load and display the image

img_path = r"colorpic.jpg"
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
print(img.shape)

cv2.imshow("Display - Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Resize the image to maintain a standard size for all the input images

std_size = (700,465) 
rs_img = cv2.resize(img, std_size)

#cv2.imshow("Display", rs_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# Load the reference dataset for color matching

columns = ["color", "color_name", "hex", "R", "G", "B"]
data_path = r'colors.csv'
ref_data = pd.read_csv(data_path, names = columns)
print(ref_data.shape)


# Function to calculate minimum distance from all colors and get the most matching color

def get_color(B,G,R):
    min_dist = abs(B - ref_data.loc[0,"B"]) + abs(G - ref_data.loc[0,"G"])
    + abs(R - ref_data.loc[0, "R"])
    matched_color = ref_data.loc[0,"color_name"]
    
    dist = 0
    
    for i in range(1,len(ref_data)):
        dist = abs(B - ref_data.loc[i,"B"]) + abs(G - ref_data.loc[i,"G"])
        + abs(R - ref_data.loc[i, "R"])
        
        if dist <= min_dist:
            min_dist = dist
            matched_color = ref_data.loc[i,"color_name"]
        
        dist = 0
    
    # print(min_dist, matched_color)
    return matched_color
    
    
# Callback function to capture the Mouse Event and display the corresponding color name

def display_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        
        b, g, r = rs_img[y, x]

        b = int(b)
        g = int(g)
        r = int(r)
        
        ''' Drawing a filled rectangle to display the color name and corresponding pixel values'''
        
        cv2.rectangle(rs_img, (20,10), (550,40), (b,g,r), -1)
        
        text = get_color(b,g,r) + " (" + "R = " + str(r) + "," + " G = " + str(g) + "," + " B = " + str(b) + ")"
        
        ''' Displaying the name of the color in the rectangle along with the pixel values'''
        
        if b+g+r >= 400:
            cv2.putText(rs_img, text, (30,30), 2, 0.5, (0,0,0), 1, cv2.LINE_AA)
        
        else:
            cv2.putText(rs_img, text, (30,30), 2, 0.5, (255,255,255), 1, cv2.LINE_AA)
        
        cv2.imshow("Display - Resized Image", rs_img)
                
cv2.imshow("Display - Resized Image", rs_img)
cv2.setMouseCallback("Display - Resized Image", display_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

