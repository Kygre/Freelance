'''
Created on Apr 12, 2017

@author: dev
'''

from enum import Enum
import os

from tkinter import *
from tkinter import colorchooser as cd
from tkinter import filedialog as fd
from pprint import pprint

class Corners(Enum):
    SQUARE = 1
    ROUNDED = 2
    CIRCLE = 3
    
def get_color(color_name):
    '''
    Returns a tuple containing color in ((red, green, blue), #hex_number)
    '''
    form_string = 'Choose %s color' % color_name
    return cd.askcolor(title= form_string)

def get_text(arg):
    return input("%s?\n" % arg)

def get_Corners():
    return Corners( int(input('Corners?\n1 - Square\n2 - Rounded\n3 - Circle\n')))

def get_boolean(arg):
    arg = arg.lower()
    return True if (arg == 'yes' or 'y') else False
    
        
    
def read_input():
    
    options = {}
    directory = ''
    
    while(not os.path.isdir(directory)):
        directory = fd.askdirectory()
        if directory:
            print("Using %s" % directory)
    
    for root, dirs, files in os.walk(directory):
        if root == directory:
            options['directory'] = [ file for file in files]
    
    color_args = ['Background', 'Text']
    string_args = ['Name of Organization', 'College Name']
    concat = 'Concatenate users yes -> y | no -> n'
    
    for string_arg in string_args:
        options[string_arg] = get_text(string_arg)
        
    for color in color_args:
        options[color] = get_color(color)
    
    corners = get_Corners()
    if not corners:
        print("Choose corner as 1, 2, or 3\n")
        try:
            corners = get_Corners()
        except:
            print("Failed to parse corner option\nDefault = " + Corners.SQUARE)
            
    options['concat'] = get_boolean(input(concat))
    
    pprint(options)
    
if __name__ == '__main__':
    
    read_input()