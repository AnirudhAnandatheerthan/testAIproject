import pandas as pd
import pandasai as  Agent
import os
os.environ['PANDASAI_API_KEY'] = '$2a$10$BUJJBqIH6JEFTCvQNgqbEubyRI3.QiBGkvO/Lwc3oEFiX.ql8/7Ga'

population_by_country = pd.DataFrame({
    "Country": ["Canada", "America", "Germanny", "India", "China"],
    "Population": ["38484834", "39848858", "4899834", "8393593834", "596518941"]
})
agent = Agent(population_by_country)
print(agent.chat('Graph this data'))