import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
e1 = cv2.getTickCount() # To count time

# Read Files one by one
directory = 'C:\\Users\\admin\\Desktop\\ImageProcessing_190520\\90_Originals\\case12_part5_ok'

FileSuffix=1
for filename in os.listdir(directory):
    if filename.endswith(".tiff"):
        basename =  filename[0:-5]
        img1 = cv2.imread(directory+'\\'+filename,0) 
        for j  in range(29):
            for i  in range(39):
                img2 = img1[(j)*100+50:(j+1)*100+50,(i)*100+50:(i+1)*100+50]           
                mask_patch = img2.copy()
                tmp1 = np.zeros((100, 100))
                tmp2 = np.zeros((100, 100))
                mean, std_dev = cv2.meanStdDev(img2, tmp1, tmp2, mask_patch)

                if mean>8:
                    print str(FileSuffix) +' .. ' + str(mean)
                    cv2.imwrite(directory+'1\\'+basename+str(FileSuffix)+'.tiff',img2)                  
                    FileSuffix=FileSuffix+1
    continue

 
