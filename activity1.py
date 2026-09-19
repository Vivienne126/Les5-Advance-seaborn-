import seaborn as sns
import matplotlib.pyplot  as plt

df=sns.load_dataset("tips")
df=df.dropna()
print(df.head())
print(df.info())

sns.barplot(x="day" , y="total_bill" , hue="sex" , data=df)
plt.title("Average total bill per day by gender")
plt.xlabel("Day")
plt.ylabel("Average Bill in rupees")
plt.show()

sns.countplot(x="day" , hue="sex" , data=df)
plt.title("Number of diners per day by gender")
plt.xlabel("Day")
plt.ylabel("Count")
plt.show()

