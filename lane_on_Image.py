'''
Created on 12 de nov de 2018

@author: aoliveir
'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
from roi import getROI
from drawLines import LaneLines

class lanedetection():
   
    # reading in an image
    image = mpimg.imread('1.jpg')
    #image = cv2.imread('solidWhiteCurve.jpg',1)
    
    height, width, channel = image.shape
    
    # printing out some stats and plotting the image
    print('This image is:', type(image), 'with dimensions:', image.shape)
    
    ##img mask data -> triangule from bottom img...pass to no array and to int 32 type int
    region_of_interest_vertices = [(0, height),(width / 2, height / 2),(width, height),]
    region_of_interest_vertices = np.array(region_of_interest_vertices)
    region_of_interest_vertices = np.int32(region_of_interest_vertices)
    
    # object of roi
    roi_img = getROI()
    
    # Convert to grayscale here.
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    
    #gray_image = cv2.medianBlur(gray_image,3)
    gray_image = cv2.GaussianBlur(gray_image,(3,3),0)
    plt.imshow(gray_image)
    plt.show()
    
    '''
    to check the usage of mean value from image
    '''
    # compute the median of the single channel pixel intensities
    sigma=0.33
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    
    print(lower,upper)
    
    
    # Call Canny Edge Detection here.
    cannyed_image = cv2.Canny(gray_image, lower, upper)
    #sobelx_image = cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=5)
    print(type(cannyed_image))
       
    #crop the cannyed img
    cropped_img = roi_img.region_of_interest(cannyed_image, region_of_interest_vertices)
    
    plt.imshow(cropped_img)
    plt.show()
    
    lines = cv2.HoughLinesP(cropped_img,rho=6,theta=np.pi/80, threshold=160, lines=np.array([]),
            minLineLength=18,maxLineGap=20)
    
    drawLanes = LaneLines()
    
    image = drawLanes.draw_lines(image, lines, [255, 0, 0], 3)
    
    print(lines)
    plt.imshow(image)
    plt.show()