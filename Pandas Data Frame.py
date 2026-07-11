#Pandas Data Frame
import pandas as pd
student={
    "Name":["Ahmed","Muhin","Raiyan","Rehnuma","Jowa","Sadik","Shafin","Anisha","Mostahid","Arisha"],
    "Dept":["CSE","EEE","ME","CSE","IPE","CSE","ME","ECE","CE","EEE"],
    "CGPA":[3.50,3.43,3.00,3.55,4.00,4.00,3.90,3.06,3.25,3.75]
}
df=pd.DataFrame(student)
print(df)
print("Student's Name With Department")
print(df[["Name","Dept"]]) #Print particular columns
print("First 5 rows:")
print(df.head())  #Print first 5 rows
print("Last 5 rows")
print(df.tail()) #Print last 5 rows
print(df.shape)  #Give the shape (10,3) of the data frame
print(df.info()) #Give details of the data frame
print(df.describe()) #Give Statistical analysis of the data frame
df["Semester"]=["First","Second","Third","Seventh","Fifth","Nineth","Third","Eighth","Fourth","Sixth"] #Add a new column
print("After adding a new column:")
print(df)
print("5th Row")
print(df.iloc[4])
print("10th row 1st column")
print(df.iloc[9,0]) #Print particular cell
print("Students with Name,Department and Semester")
print(df[["Name","Dept","Semester"]])
print(df.iloc[7])
