import numpy as np
import pandas as pd

df = pd.read_json('all_cards.json')
# print(df.columns)

land_df = df[['name', 'color_identity', 'type_line']]
# land_df.to_csv('lands.csv')
# print(land_df)
# test = land_df.loc[land_df['type_line'] == 'Land']
# print(test)
land_df.dropna()
fetches = ['Flooded Strand', 'Marsh Flats', 'Arid Mesa', 'Windswept Heath', 'Polluted Delta', 'Scalding Tarn', 'Misty Rainforest', 'Bloodstained Mire', 'Verdant Catacombs', 'Wooded Foothills']
colors = [['W', 'U'], ['W', 'B'], ['R', 'W'], ['G', 'W'], ['U','B'], ['U', 'R'], ['G','U'], ['B','R'], ['B', 'G'], ['R', 'G']]
type = ['Land','Land','Land','Land','Land','Land','Land','Land','Land','Land']
i = 0
while i < len(fetches):
    land_df.loc[land_df['name'] == fetches[i]] = [fetches[i], colors[i], type[i]]
    i += 1
# print(land_df.loc[land_df['name'] == 'Polluted Delta'])
land_df.to_csv('lands.csv')