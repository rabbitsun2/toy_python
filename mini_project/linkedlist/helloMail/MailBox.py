# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:44:14 2022

@author: user1
"""

class MailBox():
    
    def __init__(self):
        self.result = 0
        
        
    def add(self, num):
        self.result += num
        return self.result
    
def echo_test():
    print("echo")