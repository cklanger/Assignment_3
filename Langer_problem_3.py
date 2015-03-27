# -*- coding: utf-8 -*-
"""
Problem 3

Computes the two roots of the quadratic equation
a x^2 + b x + c = 0,
using three methods: 
 (i) the standard formula x=(-b+/-sqrt(b^2-4ac))/(2a),
 (ii) the alternative method x=(2c)/(-b-/+sqrt(b^2-4ac)),
and (iii) a combination of the two methods which avoids 
numerical inaccuracy.

The program for part (b) (printing out results for (i) and (ii)
for the specific equation 0.001x^2+1000x+0.001=0) is in comments.
"""
from math import sqrt
def SGN(b):
    if b>0.0:
        return 1.0
    else: 
        return -1.0
A,B,C=0.001,1000,0.001
root_1=(-B+sqrt(B*B-4.0*A*C))/(2.0*A)
root_2=(-B-sqrt(B*B-4.0*A*C))/(2.0*A)
print("method (a) x_1={} x_2={}".format(root_1,root_2))
alt_root_1=(2.0*C)/(-B-sqrt(B*B-4.0*A*C))
alt_root_2=(2.0*C)/(-B+sqrt(B*B-4.0*A*C))
print("method (b) x_1={} x_2={}".format(alt_root_1,alt_root_2))

# ------------------ GENERAL METHOD -------------------------

a=float(input("Enter the coeff. of x^2:"))
b=float(input("Enter the coeff. of x^1: "))
c=float(input("Enter the coeff of x^0: "))

Q=-0.5*(b+SGN(b)*sqrt(b*b-4.0*a*c))
x_1=Q/a
x_2=c/Q
print("general method: x_1={} x_2={}".format(x_1,x_2))

# ---------------- OUTPUT FOR PARTS (A),(B),(C) ---------------------
# method (a) x_1=-9.999894245993346e-07 x_2=-999999.999999
# method (b) x_1=-1.000000000001e-06 x_2=-1000010.5755125057

# Enter the coeff. of x^2:0.001

# Enter the coeff. of x^1: 1000

# Enter the coeff of x^0: 0.001
# general method: x_1=-999999.999999 x_2=-1.000000000001e-06
