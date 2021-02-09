# -*- coding: utf-8 -*-

from lib import schedule_parser

#def..

if __name__ == "__main__":
    keywords = ("COMPDAT","COMPDATL","DATES")
    parameters = ()
    input = "C:/Users/abali/Documents/python_1k/parser" #path
    output_csv = "C:/Users/abali/Documents/python_1k/parser_task"
    schedule_df = schedule_parser.transform_schedule(keywords, parameters, input, output_csv)