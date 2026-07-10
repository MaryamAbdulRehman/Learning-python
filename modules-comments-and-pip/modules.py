# Chapter 1: Modules,Comments & pip

import flask
import pyjokes 
#Random joke print kar sakty hain kisi aur ka code use kar k yaani pyjokes import karky.
#Yani ultimate task ko achieve kar liya

#Modules :A module is file containing code written by somebody else whuch can be imported  and used in our programs.
#pip: Pip is a package manager for python.we can use pip to install a module in our system

joke=pyjokes.get_joke()
print(joke)

#Two types of Modules
# 1.Built in MOdule(Pre installed in python)
# 2.External Module(Install using pip)       Comments ko interpreter ignore karta ha


'''We can use python as a calculator by typing python + enter on the terminal.This opens REPL (Read Evaluate Print Loop)
'''