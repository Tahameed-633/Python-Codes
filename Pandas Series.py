#Pandas series
import pandas as pd
obj=pd.Series([4,7,-5,3])
print(obj)
print(obj%2) #Modulas operation
even=obj[obj%2==0] #Data filtering
print(even)
print(obj+5) #Scalar addition
print(obj*5) #scalar multiplication