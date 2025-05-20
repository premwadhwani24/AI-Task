import cv2
import numpy as np

# Load the image
image = cv2.imread('scene.png')
if image is None:
    print("Error: Image not found. Make sure 'scene.jpg' is in the same directory.")
    exit()

# Convert the image from BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the color range for detection (e.g., red color)
lower_bound1 = np.array([0, 100, 100])  # Lower bound of HSV for red
upper_bound1 = np.array([10, 255, 255])  # Upper bound of HSV for red

# Define the second range for red color
lower_bound2 = np.array([160, 100, 100])
upper_bound2 = np.array([180, 255, 255])

# Create masks for the defined color ranges
mask1 = cv2.inRange(hsv_image, lower_bound1, upper_bound1)
mask2 = cv2.inRange(hsv_image, lower_bound2, upper_bound2)

# Combine both masks
mask_combined = mask1 | mask2

# Apply the mask to extract the detected color regions
result = cv2.bitwise_and(image, image, mask=mask_combined)

# Save the outputs
cv2.imwrite('original_image.jpg', image)
cv2.imwrite('color_mask.jpg', mask_combined)
cv2.imwrite('detected_color_regions.jpg', result)

print("Images saved as 'original_image.jpg', 'color_mask.jpg', and 'detected_color_regions.jpg'")

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Color Mask', mask_combined)
cv2.imshow('Detected Color Regions', result)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
