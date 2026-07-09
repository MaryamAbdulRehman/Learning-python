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
REPL:e.g 8*3 ha iss ko pehly read kiya .phir evaluate kiya 24 bana aur phir 24 ko print kiya aur loop yaani ab dobaara
sa hum number enter kar sakty hain 3+4 like iss tarah
'''