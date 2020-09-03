# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:08:18 2020

@author: saura
"""
import PyPDF2

with open('./PDF/dummy.pdf', 'rb') as file:      
# 'rb' is read binary, for pdf we append 'b' to it.
# so it converts the file to binary and PyPDF2 works with binary files.
    reader = PyPDF2.PdfFileReader(file)
    print(file)
    print(reader)
    print(reader.numPages)
    print(reader.getPage(0))

    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('./PDF/rotated.pdf', 'wb') as new_file:
        writer.write(new_file)

