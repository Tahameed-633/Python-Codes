import pandas as pd
student={
    "Name":["Farhan","Arisha","Shafin","Tasnim","Anisha"],
    "Dept":["CSE","EEE","ECE","IPE","NAME"]

}
df=pd.DataFrame(student)
print("Shape of the data frame",df.shape)
print(df)
print("Third row")
print(df.iloc[3])
print("Third row first column")
print(df.iloc[2,0])
print("Statistical Analysis:")
print(df.describe())
print("Add a new column:")
df["CGPA"]=[3.50,3.06,3.50,4.00,2.76]
print(df)
print("Shape of the data frame",df.shape)