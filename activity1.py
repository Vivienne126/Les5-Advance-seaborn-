import seaborn as sns
import matplotlib.pyplot  as plt

df=sns.load_dataset("tips")
df=df.dropna()
print(df.head())
print(df.info())

# sns.barplot(x="day" , y="total_bill" , hue="sex" , data=df)
# plt.title("Average total bill per day by gender")
# plt.xlabel("Day")
# plt.ylabel("Average Bill in rupees")
# plt.show()

# sns.countplot(x="day" , hue="sex" , data=df)
# plt.title("Number of diners per day by gender")
# plt.xlabel("Day")
# plt.ylabel("Count")
# plt.show()

#Part 2:Box plot , strip plot, swarm plot
# sns.boxplot(x="day" , y="total_bill" , data=df)
# plt.title("Spread of total bill per day")
# plt.xlabel("day")
# plt.ylabel("Total bill($)")
# plt.show()

# sns.stripplot(x="day" , y="total_bill" , data=df , jitter=True)
# plt.title('Every bill amt per day(sstrip plot)')
# plt.xlabel("Day")
# plt.ylabel("total bill($)")
# plt.show()

# sns.swarmplot(x="day" , y="total_bill" , data=df)
# plt.title('Every bill amt per day(swarm plot)')
# plt.xlabel("Day")
# plt.ylabel("total bill($)")
# plt.show()

#Joint plot

# sns.jointplot(x="total_bill" , y="tip" , data=df)
# plt.suptitle("Total bill vs tip" , y=1.02)
# plt.show()

# sns.jointplot(x="total_bill" , y="tip " , data=df , kind="kde" )
# plt.suptitle("total bill vs tip-kde joint plot" , y=1.02)
# plt.show()

#Pair plot

# sns.pairplot(df[["total_bill" , "tip" , "size"]])
# plt.suptitle("Pair plot-Bill,tip, and party size" , y=1.02)
# plt.show()

#Point plot and implot
sns.pointplot(x="day" , y="total_bill" , hue="sex" , data=df)
plt.title("Avg bill per day by gender")
plt.xlabel("day")
plt.ylabel("Avg bill($)")
plt.show()

#Implot
sns.implot(x="total_bill" , y="tip" , data=df)
plt.title("Total bill vs tip-Trend line")
plt.show()