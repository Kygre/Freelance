'''
Created on Apr 20, 2017

@author: dev
'''
import unittest
import os
from pprint import pprint

def get_Files(directory = ''):
    
    ext_list = {}

    for root, dirs, files in os.walk(directory):
        
        if root == directory:
            if files:
                for f in files:
                    ext = f.split(".")[1]
                    if not ext in ext_list:
                        ext_list[ext] = [f]
                    else:
                        ext_list[ext].append(f)
        
    return ext_list
    

class Test(unittest.TestCase):

    def test_bucket_init(self):
        
        directory = r'C:\Users\dev\Pictures\Empty Picture Folder'
        
        self.assertEqual({}, get_Files(directory), 'Buckets not init')
    
    def test_bucket_w_pictures(self):
        directory = r'C:\Users\dev\Pictures\Test Picture Folder'
        buckets = get_Files(directory)
        
        print("buckets\n")
        pprint(buckets)
        self.assertEqual({'jpg' : ['Sierpinski_square.jpg'] , 'png'  : ['circle-png-25308.png']}, get_Files(directory), "Failed to parse into buckets")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()