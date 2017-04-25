'''
Created on Apr 20, 2017

@author: dev
'''
from os.path import os
from pprint import pprint



def get_Files(directory = ''):
    
    ext_list = {}

    for root, dirs, files in os.walk(directory):
        
        if root == directory:
            if files:
                pprint(files)
                for f in files:
                    ext = f.split(".")[1]
                    if not ext in ext_list:
                        ext_list[ext] = []
                    else:
                        ext_list[ext].append(f)
        
    return ext_list   
        
if __name__ == '__main__':
    empty_direcotry = r'C:\Users\dev\Pictures\Empty Picture Folder'
    two_pics = r'C:\Users\dev\Pictures\Test Picture Folder'
    
    get_Files(empty_direcotry)
    pprint(get_Files(two_pics))
    