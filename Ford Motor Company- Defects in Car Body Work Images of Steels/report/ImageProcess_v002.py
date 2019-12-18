import numpy as np
import cv2
from matplotlib import pyplot as plt
e1 = cv2.getTickCount() # To count time

# Read File
FileName = 'cam3_4light_35cm_P0'
img1 = cv2.imread('case11\\' + FileName + '.tiff',0) #3000x4096
print img1.shape
img = img1[0:2000,2048:4096]
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


blur = cv2.bilateralFilter(img,9,100,100) #Large filters (d > 5) are very slow
#Bilateral filter removes textures and makes it easier to filter
# by that way, we are not removing and detail over the part.

ret,thresh2 = cv2.threshold(blur,250,255,cv2.THRESH_TOZERO_INV)
#ret,thresh3 = cv2.threshold(thresh2,5,150,cv2.THRESH_TOZERO)
ret, thresh4_bw = cv2.threshold(thresh2,5,250,cv2.THRESH_BINARY_INV)
#Otsu or other binary else tresholds did not work as good as expected.
#We are filtering BW colors  over 250
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(thresh4_bw,kernel,iterations = 1)
img_dilated = cv2.dilate(erosion,kernel,iterations=3)
img_dilated_inv_marker = (255-img_dilated)

##bgdModel = np.zeros((1,65),np.float64)
##fgdModel = np.zeros((1,65),np.float64)
##
##rect = (50,50,450,290)
##cv2.grabCut(img,img_dilated_inv_marker,rect,bgdModel,fgdModel,1,cv2.GC_INIT_WITH_RECT)
##
##mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
##img_filtered = img*mask2[:,:,np.newaxis]
img_filtered=img.copy
img_filtered[img_dilated_inv_marker==[255,0,0]]=[255,0,0]
#erosion = cv2.dilate(thresh4_bw,kernel,iterations=3)
#img_filtered = cv2.erode(erosion,kernel,iterations = 5)


titles = ['Original Image','TOZERO_INV','BW','FILTERED']
images = [img, thresh2,img_dilated_inv_marker,img_filtered]

for i in xrange(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.savefig(FileName+'_Tresholded.png',bbox_inches='tight',dpi=300)
plt.show()

#plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
#plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')

# To draw rectangle over the surface around the error
# cv2.rectangle(img,(500,500),(1000,1000),(255,0,0),50)

#cv2.imwrite('messigray.tiff',img)


