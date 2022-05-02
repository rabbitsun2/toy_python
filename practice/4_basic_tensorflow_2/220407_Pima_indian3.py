import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset/pima-indians-diabetes.csv', 
    names = ["pregnant", "plasma", "pressure", "thickness",
            "insulin", "BMI", "pedigree", "age", "class"])

plt.figure(figsize=(12,12))
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap= plt.cm.gist_heat,
 linecolor='white', annot=True)

plt.show()