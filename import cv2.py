# For Google Colab, use cv2_imshow
from google.colab.patches import cv2_imshow
import cv2

# Test OpenCV
print(cv2.__version__)  # This should print the version of OpenCV installed

# Read and display an image (replace with the actual image path)
img = cv2.imread('test_image.jpg')

# Check if the image was loaded correctly
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Display the image using cv2_imshow for Colab
    cv2_imshow(img)
