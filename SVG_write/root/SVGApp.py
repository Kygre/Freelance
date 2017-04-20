'''
Created on Apr 12, 2017

@author: dev
'''

from enum import Enum
import os
import logging

from tkinter import *
from tkinter import colorchooser as cd
from tkinter import filedialog as fd
from pprint import pprint
from _stat import filemode

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
    input_arg = input('Corners?\n1 - Square\n2 - Rounded\n3 - Circle\n')
    if input_arg:
        return Corners(int(input_arg))
    else:
        print("Default corner is %s" % Corners.SQUARE)
        return Corners.SQUARE
def get_boolean(arg):
    arg = arg.lower()
    return True if (arg == 'yes' or 'y') else False
    
def read_input():
    
    options = {}
    directory = ''
    color_args = ['Background', 'Text']
    string_args = ['Name of Organization', 'College Name']
    concat = 'Concatenate users yes -> y | no -> n\n'
    accepted_formats = {'svg', 'png'}
    
    
    while(not os.path.isdir(directory)):
        directory = fd.askdirectory()
        if directory:
            logging.info("Directory %s" % directory)            
    
    
    for root, dirs, files in os.walk(directory):
        if root == directory:
            
            all_files = [ f for f in files if os.path.splitext(os.path.join(root,f)) in accepted_formats]
    
    if not options['files']:
        error_msg = 'No files found in %s -- Program Will Exit' % directory
        logging.error(error_msg)
        raise(Exception(error_msg))
    
        
    
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
            pass
    options['concat'] = get_boolean(input(concat))
    pprint(options)
    
    return options
if __name__ == '__main__':
    
    logging.basicConfig(filename='logging.log', filemode = 'w', level = logging.DEBUG)
    options = read_input()
    
    