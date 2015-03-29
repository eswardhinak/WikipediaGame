'''
Name: parse.py
Description: This file gets the start and end articles and passes them to findPaths module
'''
import os
import findPaths

print "Beginning Program....\n"
str_begin=raw_input("Enter start point: ")
str_end=raw_input("Enter end point: ")
str_begin.replace(' ', '_')
str_end.replace(' ', '_')
findPaths.findPaths(str_begin, str_end)




