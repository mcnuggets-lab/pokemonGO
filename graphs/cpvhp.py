# linear algebra and data manipulation
import numpy as np
import pandas as pd

# for visulization
#import seaborn as sns
#from matplotlib import pyplot

try:
    df = pd.read_excel('static/graphs/pokemonGO.xls')
    data = df.drop(['Type 2', 'Image URL'], 1)
    
    names = data['Name'].tolist()
    types = data['Type 1'].tolist()
    mcp = data['Max CP'].tolist()
    mhp = data['Max HP'].tolist()
    
    type_colors = []
    type_dict = {
        "Fire": "#F08030",
        "Water": "#6890F0",
        "Grass": "#78C850",
        "Electric": "#F8D030",
        "Psychic": "#F85888",
        "Ground": "#E0C068",
        "Poison": "#A040A0",
        "Fighting": "#C03028",
        "Rock": "#B8A038",
        "Bug": "#A8B820",
        "Fairy": "#FF99CC",
        "Ghost": "#705898",
        "Dragon": "#7038F8",
        "Ice": "#98D8D8",
        "Flying": "#A890F0",
        "Steel": "#B8B8D0",
        "Normal": "#A8A878",
        "Dark": "#705848"
        }
    
    for i in range(len(data["Type 1"])):
        type_colors.append(type_dict[data["Type 1"][i]])

except:
    print("Cannot load excel file.")
    names = ''
    types = ''
    mcp = ''
    mhp = ''
    type_colors = ''