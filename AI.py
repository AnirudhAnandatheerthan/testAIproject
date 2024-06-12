import pandas as pd
from pandasai import Agent
import os
from sklearn.cluster import KMeans

os.environ['PANDASAI_API_KEY'] = '$2a$10$fG0XgS85l0mYxtWXCU/AaOlrShJVq.WIAtOpjkEUmimlbV9Utk/Ve'

Adresses = pd.read_csv('https://raw.githubusercontent.com/codeforamerica/ohana-api/master/data/sample-csv/addresses.csv')
#population_by_country = pd.DataFrame({
 #   "Country": ["Canada", "America", "Germanny", "India", "China"],
  #  "Population": ["5848894", "39848858", "4899834", "8393593834", "596518941"] })


#print(Adresses)
agent = Agent(Adresses)
#print(color_by_number)
print(agent.chat('What is the country of Redwood City??'))