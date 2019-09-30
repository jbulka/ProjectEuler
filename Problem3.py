#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Euler Project: Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import math


def is_prime(num): # tests if num is prime, but this function is computationally expensive
    
    result = True # intially assume that num is prime
    
    # if num is 2, return true
    if num == 2:
        return result
    
    # num is not 2, loop over all values between 2 and num-1
    else:
        for i in range(2, int(num)):
            if num % i == 0: # if num divisible by anything, result = False and break out of loop
                result = False
                break

    # return the answer
    return result

def main():
    
    # set number in a variable for ease of access 
    num = 600851475143
    
    # find the smallest divisors of num and compute their quotient
    for i in range(2, math.floor(num/2) + 1):
        
        # if num is divisible by i, find the quotient
        if num % i == 0:
            q = num/i
            
            # is q prime? if so, you have your answer, so break out of the loop 
            if is_prime(q) == True:
                ans = q
                break
    
    # print the answer
    print(ans)

# run the program    
if __name__ == '__main__':
    main()