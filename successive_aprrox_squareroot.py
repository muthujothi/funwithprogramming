#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 15:57:30 2018

@author: muthujothi

Finding the square root of a Positive Integer through Successive Approximation.
Guess and Check Method
Step in the size of 1/1000
Threshold in the range of 1/100th of the target
"""

x = int(input("Key in a Positive Integer whose Square Root needs to be found: "))
epsilon = 0.001
step = 0.0001
guess = 0.0
iter_cnt = 0

#As Long as the Guess is less than the target and the square of guess is greater
#then the threshold, keep walking
while (abs((guess*guess)-x) > epsilon and guess < x):
    guess = guess + step
    iter_cnt += 1

if (guess >= x):
    print ("You've Overstepped and missed to find the square root")
else:
    print ("Square Root of ", x, " is ", guess)
    print ("It took nearly ", iter_cnt, " iterations/steps to find the square root.")
    
    
    

