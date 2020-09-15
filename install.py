#!/usr/bin/python3

module_list = ["prettytable"]

def check():
    installed_list = os.poen("pip3 list").read()
    for m in module_list : 
        if m not in installed_list:
            print("Please install module: " + m)
            os.system("pip3 install " + m)
    
    