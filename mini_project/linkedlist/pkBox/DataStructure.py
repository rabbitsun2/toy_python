# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:56:09 2022

@author: user17
"""

class Node():
    
    def __init__(self):
        self.prev = None
        self.data = 0
        self.next = None
        
    def getPrev(self):
        return self.prev
    
    def setPrev(self, prev):
        self.prev = prev
        
    def getData(self):
        return self.data
        
    def setData(self, data):
        self.data = data
        
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next
        
class LinkedList():
    
    def __init__(self):
        self.head = None
        self.current = None
        self.count = 0
        
    def push(self, node):
        
        if self.head == None:
            
            #mirrorNode = Node()
            #mirrorNode.setData(node.getData())
            
            self.head = node
            #self.current = mirrorNode
            self.current = node
            
            print("링크드리스트:%s,%s" 
                  %(self.head.getData(), self.current.getData()) )
            
        else:
            cur = self.current
            cur.setNext(node)
            cur = cur.getNext()
            self.current = cur
            
    def pop(self):
        
        if self.head != None:
            cur = self.current
            
            if (cur.getPrev() != None):
                self.current = cur.getPrev()
            
            return cur
        else:
            return None
            
            