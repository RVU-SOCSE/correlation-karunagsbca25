#prg 15
import pandas as pd 
import matplotlib.pyplot as plt  
import seaborn as sns 
df2 = pd.read_csv(r"C:/Users/karun/Downloads/10prog_4laptops - 10prog_4laptops.csv")
sns.heatmap(df2.corr(numeric_only=True),annot=True)
plt.show()
