import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

from typing import Callable

PATH_DATA = 'data/'
PATH_FIGURES = 'figures/'

def timestamp() -> str:
    '''
    Returns a timestamp as a string.
    Should be safe for use as a filename on any OS.
    '''
    return str(dt.now()).replace(':', '.').replace(' ', '-')

def check_directory(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)
    return