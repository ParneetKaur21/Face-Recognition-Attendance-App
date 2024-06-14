import cv2
import os

haarcascade_path = cv2.data.haarcascades
data_directory = os.path.dirname(haarcascade_path)
print(data_directory)
