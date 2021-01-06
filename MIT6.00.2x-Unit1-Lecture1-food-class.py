# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 08:46:55 2020

MIT 6.00.2x Introduction to Computational Thinking and Data Science
UNIT 1
Lecture 1

Maybe try finding an up-to-date link of the relevant year/edition of the course
Old link - stopped working Jan 2021
https://learning.edx.org/course/course-v1:MITx+6.00.2x+3T2020/

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
# =============================================================================
# Video: Greedy Algorithms
# Class Food
# =============================================================================

class Food(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.calories = w
        
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories # in this example the cost is equal to calories, but cost can be time, money etc
    
    def density(self): # here we define a metric - we wish to maximize the value to weight ratio
        return self.getValue()/self.getCost()
    
    def __str__(self):
        return self.name + ': <' + str(self.value)\ + ', ' + str(self.calories) + '>'