'''
Created on 12 de nov de 2018

@author: aoliveir
'''
import numpy as np
import cv2



class LaneLines():
    
    def draw_lines(self,img, lines, color, thickness):
        '''
        parameters
        img, lines, color=[255, 0, 0], thickness=3
        '''    
        
        # If there are no lines to draw, exit.
        if lines is None:
            return
    # Make a copy of the original image.
        img = np.copy(img)
    # Create a blank image that matches the original in size.
        line_img = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8,)
    # Loop over all lines and draw them on the blank image.
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)
    # Merge the image with the lines onto the original.
        img = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)
    # Return the modified image.
        return img


   