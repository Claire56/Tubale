from distutils import text_file
from wordcloud import STOPWORDS, WordCloud
import re
import matplotlib.pyplot as plt

def get_file_contents(txt_file):
    with open(text_file) as f:
        contents =  f.readlines()
    return contents