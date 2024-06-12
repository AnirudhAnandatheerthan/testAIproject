import pandas as pd
from pandasai import Agent
import os
from sklearn.cluster import KMeans

os.environ['PANDASAI_API_KEY'] = '$2a$10$BUJJBqIH6JEFTCvQNgqbEubyRI3.QiBGkvO/Lwc3oEFiX.ql8/7Ga'

color_by_number = pd.DataFrame({
    "color":["Red", "Blue", "Green"],
    "number": ["one", "two", "three"]


})

agent = Agent(color_by_number)
#print(color_by_number)
response = agent.chat('What is the color of one?')
print(response)
