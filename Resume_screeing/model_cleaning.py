import re


def cleanResume(txt):
    cleanTxt = re.sub(r'http\S+', '', txt)
    cleanTxt = re.sub(r'\.', '', cleanTxt)
    cleanTxt = re.sub(r'@\S+', '', cleanTxt)
    cleanTxt = re.sub(r'#\S+', '', cleanTxt)
    # Remove special characters ($, #, etc.)
    cleanTxt = re.sub(r'[^A-Za-z0-9\s]', '', cleanTxt)
    # Remove extra whitespace
    cleanTxt = re.sub(r'\s+', ' ', cleanTxt).strip()
    stop_words = r'\b(?:on|to|the|and|in|at|for|with|of|a|an|by|as|is|are)\b'
    cleanTxt = re.sub(stop_words, '', cleanTxt).strip()

    return cleanTxt
