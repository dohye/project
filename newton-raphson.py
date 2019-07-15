# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:30:18 2018

@author: soojin
"""
 
## 1. f(x)=0 의 해 구하기 ##

# $f(x)$ 함수 지정

def f(x):
    y = x**2 - 4
    return y
    
# $f'(x)$ 함수 정의

def derivative(f, x):
    h = 0.000001   
    derivative = (f(x + h) - f(x)) / h
    return derivative

    
# newton-raphson 함수

import numpy as np

def newton_raphson(x0, ABSTOL, iterate_num):
    
    result = list()
    result.append(x0)
    
    for i in range(iterate_num):
        
        if derivative(f, x0) == 0:
            print("can't be differentiated")
        
        x = x0 - f(x0)/derivative(f, x0)
        result.append(x)       
        if np.abs(x0-x) < ABSTOL:
            print("result : ", result)
            break
        
        x0 = x
        i += 1
        
    if np.abs(f(x0)) > ABSTOL: 
        print("do not converge within the number of iterations")
        
        
## 실행 ( 초기값, 오차허용도, 반복수 지정 )
 
# 지정반복수 내에 수렴하지 않는 경우
newton_raphson(10, 5E-08, 5)

# 지정반복수 내에 수렴하는 경우
newton_raphson(10, 5E-08, 20)

# 초기값을 음수로 지정하면 그에 가까운 해를 찾게됨
newton_raphson(-10, 5E-08, 20)




###################################################

## 2. $f(x)$ 의 최소, 최대값 구하기 ##

# $g(x)$ 함수지정  ( $g(x)=f'(x)$ )

def g(x):
    y = 2*x
    return y

# newton-raphson 함수

def newton_raphson_2(x0, ABSTOL, iterate_num):
    
    result = list()
    result.append(x0)
    
    for i in range(iterate_num):
        
        if derivative(g, x0) == 0:
            print("can't be differentiated")
        
        x = x0 - g(x0)/derivative(g, x0)
        result.append(x)       
        if np.abs(x0-x) < ABSTOL:
            print(" x_list :", result, "\n","max/min value : ", f(result[-1]))
            break
        
        x0 = x
        i += 1
        
    if np.abs(g(x0)) > ABSTOL: 
        print("do not converge within the number of iterations")

        
# 실행 ( 초기값, 오차허용도, 반복수 지정 )
newton_raphson_2(5, 5E-08, 10)
