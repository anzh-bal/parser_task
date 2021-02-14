# -*- coding: utf-8 -*-
import re
import numpy
import pandas

def transform_schedule (keywords, parameters, input, output):
    """
    reads the input file .inc and transforms it to .csv schedule

    """
    return

def read_sch(path):
    file = open("test_schedule.inc")
    txt = file.read()
    return txt

#def inspect_sch():

def clean_sch(text):

    str = text.split('\n')
    new_list = []
    for i in range (len(str)):
        if re.search ('--', str [i]) == None:
            if re.search('\n', str[i]) == None:
                new_list.append(str[i])

    return new_list

a = read_sch('C:/Users/AB/Documents/study/parser_task')
clean_sch(a)


#def parse_sch():

#def extract_keyword_block():

#def extract_lines_from_keyword_block():

#def parse_keyword_block():

def parse_keyword_DATE_line(str):
    return re.sub('/','', str)

def parse_keyword_COMPDAT_line(list):
    comp = []
    for i in range(len(list)):
        if list[i] == 'COMPDAT':
            comp.append (list[i+1])
            re.split(' ', list[i+1])
        return comp

def parse_keyword_COMPDATL_line(list):
    comptl = []
    for i in range(len(list)):
        if list[i] == 'COMPDATL':
            comp.append(list[i + 1])
            re.split(' ', list[i + 1])
        return comptl

#def result_to_csv():

