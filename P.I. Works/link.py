#!/usr/bin/env python
# coding: utf-8

"""
assuming that every protocol ends with :// because url settings and every access link provided is string 
we just need to little string manipulation. 
"""
import pandas as pd
df = pd.read_csv("access.csv")
links = []
for str_ in df['Stats_Access_Link']:
    links.append(str_[str_.find('/')+2:str_.rindex('<')])

