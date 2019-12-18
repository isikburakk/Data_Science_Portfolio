import numpy as np
import cv2
from matplotlib import pyplot as plt
e1 = cv2.getTickCount() # To count time

# Read File
img = cv2.imread('case11\cam3_4light_35cm_P0.tiff',0)

#Below function displays in full screen not so usefull
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.waitKey(0) #waits a key to be pressed to proceed
#cv2.imshow('Original Image',img)
#cv2.waitKey(0) #waits a key to be pressed to proceed



e2 = cv2.getTickCount()# To count time
time = (e2 - e1)/ cv2.getTickFrequency()
print 'Time to run: ' + str(time) + ' seconds.'

##plt.imshow(img, cmap = 'gray')
##plt.xticks([]), plt.yticks([ ])  # to hide tick values on X and Y axis
##plt.show()
threshold_val = 220;

ret,thresh1 = cv2.threshold(img,threshold_val,255,cv2.THRESH_TRUNC)
ret,thresh2 = cv2.threshold(img,threshold_val,255,cv2.THRESH_TOZERO_INV)
ret,thresh3 = cv2.threshold(img,threshold_val,255,cv2.THRESH_BINARY)
ret,thresh4 = cv2.threshold(img,threshold_val,255,cv2.THRESH_BINARY_INV)
ret,thresh5 = cv2.threshold(img,threshold_val,255,cv2.THRESH_TOZERO)


titles = ['Original Image','TRUNC','TOZERO_INV','BINARY','BINARY_INV','TOZERO']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()

#plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
#plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')

# To draw rectangle over the surface around the error
# cv2.rectangle(img,(500,500),(1000,1000),(255,0,0),50)

#cv2.imwrite('messigray.tiff',img)


