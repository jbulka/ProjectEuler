#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Euler Project: Problem 1

Problem 1: If we list all the natural numbers below 10 that are multiples of 3 
or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
    
"""

def main():
    
    # initialize answer
    ans = 0
    
    # loop over values
    for i in range(1, 1000):
        
        # if divisible by 3 or 5, add it to answer
        if i%3 == 0 or i%5 == 0:
            ans = ans + i
            
        # if not, continue to next number
        else:
            continue
        
    # print the result
    print(ans)
    
# run the program
if __name__ == '__main__':
    main()
        
        

