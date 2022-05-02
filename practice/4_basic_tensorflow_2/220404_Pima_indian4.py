import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset/pima-indians-diabetes.csv', 
    names = ["pregnant", "plasma", "pressure", "thickness",
            "insulin", "BMI", "pedigree", "age", "class"])

grid = sns.FacetGrid(df, col='class')
grid.map(plt.hist, 'plasma', bins=10)
plt.show()