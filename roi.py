'''
Created on 12 de nov de 2018

@author: aoliveir
'''
import numpy as np
import cv2
import matplotlib.pyplot as plt

class getROI():
    
    def region_of_interest(self,img, vertices):
        
        #vertices = np.array([vertices], dtype=np.int32)
        
        # Define a blank matrix that matches the image height/width.
        mask = np.zeros_like(img)
       
        # Retrieve the number of color channels of the image.
        #channel_count = img.shape[2]
        
        # Create a match color with the same color channel counts.
        match_mask_color = (255,) * 1
          
        # Fill inside the polygon
        cv2.fillPoly(mask, [vertices], match_mask_color)
        
        # Returning the image only where mask pixels match
        masked_image = cv2.bitwise_and(img, mask)
                
        return masked_image
    
    