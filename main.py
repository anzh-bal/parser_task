# -*- coding: utf-8 -*-

from lib import schedule_parser

#def..

if __name__ == "__main__":
    keywords = ("COMPDAT","COMPDATL","DATES")
    parameters = ()
    input = "C:/Users/AB/Documents/study/parser_task" #path
    output_csv = "C:/Users/AB/Documents/study/parser_task"
    schedule_df = schedule_parser.transform_schedule(keywords, parameters, input, output_csv)