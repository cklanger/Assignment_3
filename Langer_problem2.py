# -*- coding: utf-8 -*-
"""
PHYS 50733 Assignment #3
Problem 2
Computes e^(-x) 4 different
ways and plots the results. 
The decimal module is used
to deal with the large numbers
in computing the series expansions
in parts (b) and (c). Parts (a)
and (d) yield values equal in the
precision of the computer. When plotted,
part (a) points are covered by part (d) points.
See comments on the end of this program for
individual outputs of each method.
@author: Cameron Langer
"""
from math import exp,fabs
from numpy import array
from pylab import plot,xlabel,ylabel,ylim,xlim,show,legend
from decimal import getcontext,Decimal     
getcontext().prec=100 # sets precision to 100 decimal places
def factorial(n):
    f=1.0
    for k in range(1,n+1):
        f *=k
    return f
def inverse(x):
    return 1.0/x
r_x=[]
r_y=[]
r_a=[]
r_b=[]
r_c=[]
r_d1=[]
r_d2=[]
x=0.0
# compute using math function
for i in range(1,22):
    r_x.append(-x)              # this list has values x=0 to x=-100
    r_y.append(x)               # this list has values x=0 to x=100
    x += 5.0
r_a=list(map(exp,r_x))    # this list now has exp(-x) for 0-100
# compute using series expansion
err=Decimal(1.0e-12)
r_b.append(1.0)         # for e^0=1
y=Decimal(5.0)
for j in range(1,21):
    expansion=Decimal(0.0)
    nth_term=Decimal(1.0)
    epsilon=Decimal(1.0e-3)
    n=1
    while(fabs(nth_term)>epsilon):
        expansion = Decimal(expansion + nth_term)
        nth_term=Decimal(pow(Decimal(-1.0),Decimal(n))*Decimal(pow(y,Decimal(n)))*Decimal(pow(Decimal(factorial(n)),Decimal(-1.0))))
        n += 1
    r_b.append(float(expansion))
    y = Decimal(y) + Decimal(5.0)
# r_b now has the series expansion for 0-100
# compute using the other expansion
z=0.0
error=Decimal(1.0e-8)
for p in range(1,22):
    q=Decimal(1.0)
    summation=Decimal(0.0)
    nth_term=Decimal(1.0)
    while(fabs(nth_term)>error):
        summation = Decimal(summation+nth_term)
        nth_term = Decimal(-nth_term)*Decimal(z)/Decimal(q)
        q = Decimal(q)+Decimal(1.0)
    r_c.append(float(summation))
    z = Decimal(z)+Decimal(5.0)
# r_c now has the summation for 0-100
# compute using exp(-x)=1/exp(x)
r_d1=list(map(exp,r_y))          # list has exp(x) for x=0 to x=100
r_d2=list(map(inverse,r_d1))      # list has 1/exp(x) for x=0 to x=100
array_r_y=array(r_y)             # convert the lists to arrays 
array_r_a=array(r_a)             # was having trouble plotting the lists
array_r_b=array(r_b)             # so I converted them to arrays...
array_r_c=array(r_c)
array_r_d2=array(r_d2)
plot(array_r_y,array_r_a,"ko",label="part (a)")
plot(array_r_y,array_r_b,"ro",label="part (b)")
plot(array_r_y,array_r_c,"go",label="part (c)")
plot(array_r_y,array_r_d2,"ys",label="part (d)")
xlim(0.0,101.0)
ylim(-1.0e-8,1.0e-5)
xlabel("x axis")
ylabel("exp(-x)")
legend()
show()
#######################################################################
# comments on the plot
# part (a) and part (d) match within precision
# so on the plots part (a) points are covered by part (d) points
# all methods work for x=0 to x=20
# part (b) fails at x~30
# part (c) fails at x~25
# but part (c) remains near zero, whereas part (b) diverges
#######################################################################
# FOR INDIVIDUAL OUTPUTS
#######################################################################
# output of the program
# for part (a) uncomment next 2 lines
# print(r_a)
# output is 
# [1.0,
# 0.006737946999085467, 
# 4.5399929762484854e-05,
# 3.059023205018258e-07,
# 2.061153622438558e-09, 
# 1.3887943864964021e-11, 
# 9.357622968840175e-14, 
# 6.305116760146989e-16, 
# 4.248354255291589e-18,
# 2.8625185805493937e-20, 
# 1.9287498479639178e-22,             best way (with (d)) of computing e^(-x)
# 1.2995814250075031e-24, 
# 8.75651076269652e-27, 
# 5.900090541597061e-29, 
# 3.975449735908647e-31, 
# 2.6786369618080778e-33, 
# 1.8048513878454153e-35,
# 1.2160992992528256e-37,
# 8.194012623990515e-40, 
# 5.5210822770285325e-42, 
# 3.720075976020836e-44]
######################################################################
# for part (b) uncomment the next line
# print(r_b)
# output is 
#[1.0, 
# 0.006267311767056152, 
# -0.00024578346162229845, 
# 0.0005289386660091191, 
# 0.0003114317378328578, 
# -0.0005445851318046972, 
# -0.0003055121670808201, 
# 0.003070915353055089,              things go bad at x~30 to x~35
# 0.7758490486587034, 
# 173.6762513043818, 
# 24655.92390812677, 
# 2545272.1141463434, 
# 170234239.9750051, 
# -6626241829.76514, 
# -4602915286945.866, 
# -914684323263062.6,
#  -1.2623160893730192e+17,
# 4.3653233476680594e+20, 
# 7.913742053269938e+24,
#  8.047317277868398e+28, 
# 5.091429782491435e+32]
######################################################################
# for part (c) uncomment the next line
# print(r_c)
# output is 
# [1.0,
# 0.006737943884296798,
# 4.5402342097432606e-05,
#  3.089078690372437e-07, 
# 4.742252930411405e-09, 
# -6.895328452694828e-09,           things go bad at x~25
# -4.897564860806431e-09, 
# -3.3675403337254678e-09, 
# 7.035655329832404e-09, 
# 4.6479800629375745e-09, 
# 3.054341892625091e-09,
#  -5.99169101267145e-09, 
# -3.893848332013434e-09, 
# 7.460216726023178e-09,
#  4.826193098482148e-09,
#  3.1235105284907136e-09,
#  -5.88415710256265e-09,
#  -3.8036539908800106e-09,
#  7.101616629991327e-09, 
# 4.590399954517563e-09,
# 2.9697206648373146e-09]
######################################################################
# for part (d) uncomment the next line
# print(r_d2)
# output is 
# [1.0, 
# 0.006737946999085467,
# 4.539992976248485e-05,
# 3.059023205018258e-07,
# 2.061153622438558e-09,
# 1.388794386496402e-11,              results for 1/e^(x) are
# 9.357622968840174e-14,             just as good as e^(-x)
# 6.305116760146989e-16,
# 4.248354255291589e-18,
# 2.8625185805493937e-20,
# 1.928749847963918e-22,
# 1.299581425007503e-24,
# 8.75651076269652e-27,
# 5.900090541597061e-29,
# 3.975449735908647e-31,
# 2.678636961808078e-33,
# 1.8048513878454153e-35,
# 1.2160992992528256e-37,
# 8.194012623990515e-40,
# 5.5210822770285325e-42,
# 3.7200759760208356e-44]
