'''
Created on Apr 12, 2017

@author: dev
'''

from enum import Enum
import logging
import os
from pprint import pprint
from tkinter import *
from tkinter import colorchooser as cd
from tkinter import filedialog as fd

from svgwrite import text, Drawing, cm, mm
from svgwrite.shapes import Rect, Line
import svgwrite
from fileinput import filename

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
    try:
        return Corners(int(input_arg))
    except:
        print("Default is %s" % Corners.SQUARE)
        logging.info("Default corner selected %s"  % Corners.SQUARE)
        return Corners.SQUARE
def get_boolean(arg):
    args = arg.lower()
    
    if not args:
        return False
    elif (args == 'yes' or 'y'):
        return True 
    else:
        logging.info("Concat user input option empty. Defaulting to false")
        return False
    
def get_insignia():
    form_string = "Choose insignia image file"
    return fd.askopenfilename(title = form_string)

def get_Files(directory = ''):
    
    classes = ['senior', 'junior', 'sophomore', 'freshman']
    class_list = {'officer' : {cls : list() for cls in classes}, 
                'nonofficer' : {cls : list() for cls in classes}}
    
    for root, dirs, files in os.walk(directory):
        
        if root == directory:
            if files:
                for file in files:
                    '''
                    ext = f.split(".")[1]
                    if not ext in ext_list:
                        ext_list[ext] = [f]
                    else:
                        ext_list[ext].append(f)                    
                
                    '''
                    
                    # NAME - Officer/NonOfficer - Year In School - Position
                    file_info = [ x.lower() for x in file.split(' - ')]
                    officer, year = file_info[1], file_info[2] 
                    class_list[officer][year].append(file)
    
    
    return class_list


def draw(output_file, options):
    size_x, size_y = options['dimensions']
    dwg = Drawing(filename= output_file, size = (size_x, size_y))
    
    #background
    dwg.add(Rect(insert= (0,0), size=  (size_x,size_y), fill = options['Background'][1]))
    # border
    dwg.add(Rect(insert = (10,10) , size = ('97%','97%'), stroke_width = options['Border'], stroke= 'black', fill = 'white'))
    
    dwg.save()

def read_input():
    
    options = {}
    directory = ''
    color_args = ['Background', 'Text']
    string_args = ['Name of Organization', 'College Name']
    concat = 'Concatenate users yes -> y | no -> n\n'
    
    
    while(not os.path.isdir(directory)):
        directory = fd.askdirectory()
        if directory:
            logging.info("Directory %s" % directory)            
    
    options['directory'] = directory
    
    options['files'] = get_Files(directory)
    
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
    options['corner'] = corners
    
    options['concat'] = get_boolean(input(concat))
    
    try:
        options['Border'] = int(input("Border in pixels\n"))
    except:
        logging.error("Failed to parse border size\nDefault to zero pixels")
        options['Border'] = 0
    
    try:
        height, width = input("Image Height and Width as #x#\n").split('x')
        
        options['dimensions'] = int(height), int(width)
    except:
        logging.error("Failed to parse Image Height and Width")
        options['dimensions'] = (800, 600)
    
    try:
        options['year'] = input("Year\n")
    except:
        logging.error("Failed to parse year")
        logging.info("Defaulting to current year")
    try:
        options['separation'] = input("Path to Seperation image\n")
        
        for quote in ['\'', '\"']:
            if options['separation'][0] == quote:
                
                options['separation'] = options['separation'].split(quote)[1]
                break
    except:
        logging.error("Failed to parse Image height and width") 
        options['Separation'] = "Solid_white.svg.png"    
       
    try:
        options['insignia'] = get_insignia()
    except:
        logging.error("Failed to choose insignia image")
        options['insignia'] = 'Insignia.png'
    
    return options

if __name__ == '__main__':
    
    # "C:\Users\dev\Documents\GitHub\Freelance\SVG_write\root\Solid_white.svg.png"
    import pickle
    debug = True
    
    if debug:
        logging.basicConfig(filename='logging.log', filemode = 'w', level = logging.DEBUG)
        with open('save.p', 'rb') as save:
            options = pickle.load(save)
    else:
        logging.basicConfig(filename='logging.log', filemode = 'w', level = logging.INFO)
        options = read_input()
        
        with open('save.p', "wb") as save:
            pickle.dump(options, save)
    
    # sort files into class buckets -- Check
    pprint(options)
    out_file = 'testing.svg'
    # draw in order w/ border 
    draw(out_file, options)
