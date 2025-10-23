import pandas as pd
import numpy as np

dict1 = {
    "Name" : ["Naman","Manan","Raman"],
    "Grades" : ['A','B','C']
}
Data = pd.DataFrame(dict1)

Grade = {"A":1,"B":2,"C":3}

Data['Grades']=Data['Grades'].map(Grade)

