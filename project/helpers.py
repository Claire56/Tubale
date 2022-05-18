from distutils import text_file
from string import punctuation
from wordcloud import STOPWORDS, WordCloud
import re
import matplotlib.pyplot as plt


class Utils:
    punctuation = r'[\.,#\-!?:/]'


def get_file_contents(txt_file):
    with open(txt_file) as f:
        contents =  f.readlines()
    return contents

def remove_punctuation(text):
    revised_text = re.sub(Utils.punctuation, '',text)
    return revised_text