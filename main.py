# -*- coding: utf-8 -*-

from lib import schedule_parser

#def..

if __name__ == "__main__":
    keywords = ("COMPDAT","COMPDATL","DATES")
    parameters = ()
    # TODO: абсолютные пути - зло, которое перестанет работать на другом компьютере или при смене папки. Лучше храни входные файлы во вложенной папке в проекте
    input = "C:/Users/AB/Documents/study/parser_task" #path
    output_csv = "C:/Users/AB/Documents/study/parser_task"
    schedule_df = schedule_parser.transform_schedule(keywords, parameters, input, output_csv)
    
    #TODO: в проект не скопирован тест. Если я копирую тест из своей папки, то даже с исправлением всех путей твой код его не проходит
