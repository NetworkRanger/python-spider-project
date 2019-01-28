#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/28 8:03 PM

import os
import pyocr
from PIL import Image
from pytesseract import pytesseract

image = Image.open('code.png')
pytesseract.tesseract_cmd = 'c:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
code = pytesseract.image_to_string(image)
print code