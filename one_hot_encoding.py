import pandas as pd
import numpy as np

dict2 = {
    "Name" : ["Naman","Manan","Raman","Arsh","Ankush"],
    "Colour" : ['Red','Red','Yellow','Green','Yellow']
}

data=pd.DataFrame(dict2)
 
unique_colour = []
for i in data['Colour']:
    if i not in unique_colour:
        unique_colour.append(i)

for colour in unique_colour:
    data[f'Colour_{colour}'] = [1 if col== colour else 0 for col in data['Colour']]

data = data.drop('Colour', axis=1)