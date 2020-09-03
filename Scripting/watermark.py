# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:53:26 2020

@author: saura
"""
import PyPDF2

template = PyPDF2.PdfFileReader(open('./Watermark/super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('./Watermark/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

with open('./Watermark/watermarked_output.pdf', 'wb') as file:
  output.write(file)

