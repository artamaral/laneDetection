'''
Created on 13 de nov de 2018

@author: aoliveir
'''
import math
import numpy as np
from drawLines import LaneLines



class allLines():
    
    def lineGroup(self,lines,image):
        
        left_line_x = []
        left_line_y = []
        right_line_x = []
        right_line_y = []
        for line in lines:
            for x1, y1, x2, y2 in line:
                slope = (y2 - y1) / (x2 - x1) # <-- Calculating the slope.
                if math.fabs(slope) < 0.5: # <-- Only consider extreme slope
                    continue
                if slope <= 0: # <-- If the slope is negative, left group.
                    left_line_x.extend([x1, x2])
                    left_line_y.extend([y1, y2])
                else: # <-- Otherwise, right group.
                    right_line_x.extend([x1, x2])
                    right_line_y.extend([y1, y2])
                    
        #generate a linear function that match the two given spaces (x and y) for each group
        poly_left = np.poly1d(np.polyfit(left_line_y,left_line_x,deg=1))
        poly_right = np.poly1d(np.polyfit(right_line_y,right_line_x,deg=1))
        
        #Where to start to generate the lines
        min_y = int(image.shape[0] * (3 / 5)) # <-- Just below the horizon
        max_y = image.shape[0] # <-- The bottom of the image     
        
        right_x_start = int(poly_right(max_y))
        right_x_end = int(poly_right(min_y))
        
        left_x_start = int(poly_left(max_y))
        left_x_end = int(poly_left(min_y))
        
        #draw generated lines to the image
        
        drawLanes = LaneLines()
    
        image = drawLanes.draw_lines(image,[[left_x_start, max_y, left_x_end, min_y],
                                      [right_x_start, max_y, right_x_end, min_y]],[255, 0, 0], 3)
        
        image = drawLanes.draw_lane(image,[[left_x_start, max_y, left_x_end, min_y],
                                      [right_x_start, max_y, right_x_end, min_y]], 3)    
          
        
        return image          