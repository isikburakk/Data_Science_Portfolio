import numpy as np
import cv2
from matplotlib import pyplot as plt
e1 = cv2.getTickCount() # To count time

# Read File
FileName = 'cam4_4light_35cm_P1'
img1 = cv2.imread('case11\\' + FileName + '.tiff',0) #3000x4096
print img1.shape
img = img1[0:2000,2048:4096]

e2 = cv2.getTickCount()# To count time
time = (e2 - e1)/ cv2.getTickFrequency()
print 'Time to run: ' + str(time) + ' seconds.'


blur = cv2.bilateralFilter(img,9,100,100) #Large filters (d > 5) are very slow
#Bilateral filter removes textures and makes it easier to filter
# by that way, we are not removing and detail over the part.

ret,thresh2 = cv2.threshold(blur,250,255,cv2.THRESH_TOZERO_INV)
ret, thresh4_bw = cv2.threshold(thresh2,5,250,cv2.THRESH_BINARY_INV)
#Otsu or other binary else tresholds did not work as good as expected.
#We are filtering BW colors  over 250
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(thresh4_bw,kernel,iterations = 1)
img_dilated = cv2.dilate(erosion,kernel,iterations=3)
img_dilated_inv_marker = (255-img_dilated)
mask = img_dilated_inv_marker+2
mask[mask>1] = 0
## Segmented image, masked pixels are 0
filtered_img = img*mask
print filtered_img[0,10]
print filtered_img[1999,10]



##Plot ALL
titles = ['Original Image','TOZERO_INV_BLURED','BW','FILTERED']
images = [img, thresh2,img_dilated,filtered_img]

for i in xrange(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.savefig(FileName+'_Tresholded.png',bbox_inches='tight',dpi=300)
plt.show()


# To draw rectangle over the surface around the error
# cv2.rectangle(img,(500,500),(1000,1000),(255,0,0),50)



