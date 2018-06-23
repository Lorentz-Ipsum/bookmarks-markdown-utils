#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

usage:
'python find_replace_clean_html.py <html file>'

Title: Find / Replace in HTML

Description:
This script finds and replaces or removes certain html tags.
It can be ran after
- exporting an html file from Evernote
- "clearning" html (I used https://html-cleaner.com/)
"""
import os, json, sys

from replacer import replacer
from create_file import create_file

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
from get_config import get_json_config

def get_replaced_line(line):
    '''This function is file-specific
    '''
    to_delete = [
        ['<div> </div>', ''],
        ['<p></p>', ''],
        ['<div>', ''],
        ['</div>', '']
    ]
        
    to_replace = [
        ['<a', '</p>\n<a'],
        ['</a>', '</a>\n - ']
    ]
    if line == '':
        return line
    
    line = line.replace('<div><br/>', '<p>')
    line = replacer(to_delete, line)
    line = line.strip()

    if line == '':
        return line
    
    return replacer(to_replace, line) + '\n'

def main():
    html_file = sys.argv[1]

    config = get_json_config()

    user_output_path = sys.argv[2]
    if user_output_path:
      outputlocation = user_output_path
    else:
        output_filename = 'evernote_output.html'
        outputlocation = os.path.join(config['directories']['bookmarksRootDir'], output_filename)

    create_file(outputlocation, 'w', html_file, get_replaced_line)

if __name__ == '__main__':
    main()
