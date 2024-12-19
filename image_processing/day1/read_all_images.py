# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:42:45 2024

@author: abodo
"""

import cv2
import glob

path = "../images/test_images/aeroplane/*"

for file in glob.glob(path):
    a = cv2.imread(file)
    cv2.imshow("Original image", a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(a)
    c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imshow("Color image", c)
    cv2.waitKey(0)
    cv2.destroyAllWindows()