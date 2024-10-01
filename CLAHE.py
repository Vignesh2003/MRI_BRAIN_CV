import cv2
import numpy as np
import os

def apply_clahe(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(image)

# Example usage for processing all images in a folder
def preprocess_images(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            clahe_img = apply_clahe(img)
            cv2.imwrite(os.path.join(output_folder, filename), clahe_img)
