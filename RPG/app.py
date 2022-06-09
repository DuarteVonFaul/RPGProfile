from pickle import TRUE
from urllib.robotparser import RequestRate
from flask import Flask
from .resources import userAcess


app = Flask("",template_folder="./templates",static_folder='./static')

userAcess.init(app)