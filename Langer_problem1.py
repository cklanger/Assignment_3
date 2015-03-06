# -*- coding: utf-8 -*-
"""
PHYS 50733 Assignment #3
Problem 1
reads the data from "stm.txt"
and makes a density plot of the 
values.
@author: Cameron Langer
"""
from pylab import imshow,gray,colorbar,show,xlabel,ylabel
from numpy import loadtxt

data=loadtxt("stm.txt",float)
imshow(data,origin="lower")
gray()
xlabel("x position")
ylabel("y position")
colorbar()
show()

