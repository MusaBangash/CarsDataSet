import pandas as pd



df=pd.read_csv('data.csv')

print(df)

print(df.head())
print(df.shape)


#instruction for cleaning data
#find all null value in dataset if there is null fill with mean 

print(df.isnull().sum())


print(df['Cylinders'].fillna(df['Cylinders'].mean(),inplace=True))



#check what are the different type of make are there in our dataset

print(df.head(2))
print(df['Make'].value_counts())


#instruction filtering show all record where origin asia europe

print(df.head(2))
print(df['Origin'].isin(['Asia','Europe']))



#instruction removing unwanted records
#remove all the records where weight is above 4000
print(df.head(2))
#print(df['Weight']>4000)

print(df['Type']=='SUV')
print(df[df['Type']=='SUV'])




#instruction apply function on column
#increase all the values of mpg city column by 3

print(df.head(2))
df2=df['MPG_City']=df['MPG_City'].apply(lambda x:x+3)
print(df2)
