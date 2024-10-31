from flask import Flask

app=Flask(__name__)

from Resume_screeing import route
from .model_cleaning import cleanResume
from .model_loader import load_model