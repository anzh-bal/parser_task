# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame
from lib import schedule_parser


if __name__ == "__main__":
    keywords = ("COMPDAT","COMPDATL","DATES")
    parameters = ()
    input = 'test_schedule.inc'
    a = schedule_parser.read_sch(input)
    a = schedule_parser.clean_sch(a)
    schedule_df = DataFrame(schedule_parser.parse_schedule(a))#, columns=["date", "Well name","Local grid name","I","J","K upper","K lower", "Flag on connection","Saturation table","Transmissibility factor","Well bore diameter","Effective Kh","Skin factor","D-factor","Dir_well_penetrates_grid_block","Press_eq_radius"])
    print(schedule_df)
    #schedule_df = schedule_parser.parse_schedule(input)
    schedule_df.to_csv('output.csv', index = False, header = False)