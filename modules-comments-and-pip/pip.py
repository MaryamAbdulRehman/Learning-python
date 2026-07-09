1.#Install an external module and use it to perform an operation of your interest 

#Ya python text to speech k liye use hota ha module.Yahan jo bhi type karain gy wo ya boly ga
import pyttsx3
engine = pyttsx3.init()
engine.say("I like your nature.You are sooooo beautiful kind and pretty girl")
engine.runAndWait()

2.#Write a program to print the contents of a dictionary using the os module .

import os

# Specify the directory you want to list. Use '.' for the current directory.
directory_path = "/"

# 1. Get the list of contents
contents = os.listdir(directory_path)

# 2. Print the dictionary (the list of names)
print(contents)

# Optional: Print the path of the directory you are listing
print(f"\nListing contents of: {os.path.abspath(directory_path)}")
