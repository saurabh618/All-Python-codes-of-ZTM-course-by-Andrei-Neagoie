# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:49:36 2020

@author: saura
"""
from translate import Translator

with open('translate.txt', mode = 'r') as my_file:
    text = my_file.read()

translator= Translator(to_lang="es")
translation = translator.translate(text)

print(translation)