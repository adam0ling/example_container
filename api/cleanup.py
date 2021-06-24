import pandas as pd
import numpy as np
import regex
import sqlalchemy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import matplotlib.pyplot as plt
from datetime import date
import matplotlib.colors as mcolors

# Quick analysis of the whole receipt name to remove worst receipt names 

def remove_special_characters(x):
    """ Removes all special characters except: ' & - . , / % : and spaces. Removes spaces from beginings and endings"""
    return regex.sub("[^-&.,/%:'\p{L}0-9\s]", '', str(x)).strip()