#impoty libires

from deepface import DeepFace
import cv2
import matplot.pyplot as plt

#load imaes
img1=cv2.imread('C:\document')
plt.imshow(img1[:,:,::-1])
plt.show()

#compare images
result=DeepFace.verify(img1,img2)

#display results
print("is same face", result["verified"])



