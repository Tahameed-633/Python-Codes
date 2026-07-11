#Distionary to pandas series
import pandas as pd
student={
    "Name":"Tahameed",
    "Dept":"CSE",
    "Age":"24"
}
obj=pd.Series(student)
print(obj)