# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:07:32 2019

@author: Jacky
"""

from pypexels import PyPexels
api_key = '' #Insert API key here

# instantiate PyPexels object
py_pexels = PyPexels(api_key=api_key)

search_results = py_pexels.search(query='dog', per_page=40)
while True:
    for photo in search_results.entries:
        print(photo.id, photo.photographer, photo.url)
    if not search_results.has_next:
        break
    search_results = search_results.get_next_page()