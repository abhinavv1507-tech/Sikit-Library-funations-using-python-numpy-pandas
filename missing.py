import pandas as pd
import numpy as np

dict2 = {
    "Name" : ["Naman","Manan","Raman","Arsh","Ankush","Aman","dhruv"],
    "Marks" : [45,77,None,89,None,56,99]
}

data=pd.DataFrame(dict2)


choice =int(input('''which imputation techique you want
      1. Mean Imputation
      2. Median Imputation
                Enter  :   '''))

if (choice==1):
    mean_val_col = data['Marks'].mean()
    data['Marks'] = data['Marks'].fillna(mean_val_col)

elif (choice==2):
    median_val_col = data['Marks'].median()
    data['Marks'] = data['Marks'].fillna(median_val_col)
    
else:
    print("Invalid choice")




