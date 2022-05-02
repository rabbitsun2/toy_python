import pandas as pd

df = pd.read_csv('dataset/pima-indians-diabetes.csv', 
    names = ["pregnant", "plasma", "pressure", "thickness",
            "insulin", "BMI", "pedigree", "age", "class"])

#print(df.head(5))
#print(df.tail(5))

#print(df.info())

#print(df.describe())
print(df[['pregnant', 'class']])