# -*- coding: utf-8 -*-
import re
import numpy as np
import pandas
import pytest



def read_sch(text: str):
    with open(text) as text:
        text = text.read()
    return text

#def inspect_sch():


def clean_sch(text: str):

    text = re.sub(r'--\s.*', '', text)
    text = re.sub(r'\s*\n+', '\n', text)
    return text


def parse_schedule(text: str):   #, keywords_tuple = ("DATES", "COMPDAT", "COMPDATL"): Tuple[str]) #-> List[List[str]]:

    """
    returns keywords text blocks ending with a newline "/"
    @param text: cleaned input text from .inc file
    @param keywords_tuple: a tuple of keywords we are interested in (DATES, COMPDAT, COMPDATL, etc.)
    @return: list keywords text blocks ending with a newline "/"
    """
    keywords_tuple = ("DATES", "COMPDAT", "COMPDATL")
    a = read_sch(text)
    a = clean_sch(a)
    clean = parse_default(a)   #clean text
    list_dates_compdat = extract_keyword_block(clean)
    compdat = []
    dates = []
    #print(list_dates_compdat)
    for i in range(len(list_dates_compdat)):
        if (re.search(r'DATES', list_dates_compdat[i])) is None:
            if len(dates)==0:
                dates.append(np.nan)
                compdat.append(np.nan)
            else:
                dates.append(dates[-1])
                compdat.append(dates[-1])
            if (re.search(r'COMPDAT', list_dates_compdat[i])) is not None:
                compdat.append(parse_keyword_COMPDAT_line (re.sub(r'COMPDAT\s+', '', list_dates_compdat[i])))
            elif (re.search(r'COMPDATl', list_dates_compdat[i])) is not None:
                compdat.append(parse_keyword_COMPDAT_line (re.sub(r'COMPDATl', '', list_dates_compdat[i])))
        else:
            dates.append(parse_keyword_DATE_line(re.sub(r'DATES', '', list_dates_compdat[i])))
            compdat.append(parse_keyword_DATE_line(re.sub(r'DATES', '', list_dates_compdat[i])))


    print(compdat)

    result_to_csv(compdat)

    return list_dates_compdat


def extract_keyword_block(text: str):
    blocks = re.split('/\s+/\n', text)  # divided on blocks
    # выбросить ненужные блоки
    useful_blocks = []
    for i in range(len(blocks)):
        words = re.search(r'DATES|COMPDAT|COMPDATL', blocks[i])
        if words is not None:
            useful_blocks.append(blocks[i])
    return useful_blocks



def parse_keyword_DATE_line(date_line: str):
    date_line = re.sub(r"\s+/$", "", date_line)
    date_line = re.sub(r"\n", "", date_line)
    return date_line


def parse_keyword_COMPDAT_line(well_comp_line: str):
    well_comp_line = re.sub(r"'|(\s+/$)", "", well_comp_line)
    #well_comp_line = re.split('/', well_comp_line)
    well_comp_line = re.split("\s+", well_comp_line)
    well_comp_line.insert(1, np.nan)
    return well_comp_line


def parse_keyword_COMPDATL_line(well_comp_line: str):
    well_comp_line = re.sub(r"'|(\s+/$)", "", well_comp_line)
    well_comp_line = re.split("\s+", well_comp_line)

    return well_comp_line


def parse_default(well_comp_line: str):
    def f(match):
        r = match.group(0)
        r = re.sub('\*', '', r)
        return str(int(r) * " default ")
    well_comp_line = re.sub('(\d+\*)', f, well_comp_line)
    return well_comp_line

def result_to_csv(text):#: list[list[str]]):
    import csv
    with open('output.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in text:
            csv_writer.writerow([item])



parse_schedule('../test_schedule.inc')
