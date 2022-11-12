import pandas as pd

with open('table.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('table.csv', encoding='utf-8', index=False)