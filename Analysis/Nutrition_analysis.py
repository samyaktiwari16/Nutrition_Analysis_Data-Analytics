import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_context("talk")

file = r"/home/samyak/data_analytics/Analysis/supplement_impact_data.csv"
dataframe = pd.read_csv(file)
dataframe = dataframe.fillna(0)
print(dataframe.info()) 
print(dataframe.describe()) # Provide statistical summary of the dataset
print(dataframe.size) # This will tell number of entries in the dataset

# ****************************************  This graph is visualizing how many people are in each age category and also classify according to gender  ****************************************

age_categorization = dataframe.groupby('Age')["Gender"].value_counts().reset_index(name='Count')

sns.barplot(
    data = age_categorization,
    x = 'Age',
    y = 'Count',
    hue = "Gender"
)
plt.title("Number of People in each Age Category by Gender")
plt.xlabel("\nAge")
plt.ylabel("\nNo. of People")
plt.xticks(rotation=40)
plt.tight_layout()
plt.show()

# ****************************************  End  ****************************************

Benefit_Category = dataframe.groupby("Primary_Benefit").size().reset_index(name="Count")
 

# ****************************************  This graph will tell how many people are in each primary benefit category  ****************************************

sns.lineplot(
    data=Benefit_Category,
    x="Primary_Benefit",
    y="Count",
    marker="o",
    color="orange"
)

plt.title("Number of People in each Primary Benefits")
plt.xlabel("\nPrimary Benefits")
plt.ylabel("\nNo. of People")

plt.xticks(rotation=40)
plt.tight_layout()
plt.show()

# ****************************************  End  ****************************************

Male = dataframe[dataframe["Gender"] == "Male"].sort_values(by="Age", ascending=True)

count = dataframe["Gender"].value_counts()

# New column is created 
dataframe["Increased_WT"] = dataframe["Final_WT"] - dataframe["Initial_WT"]

# ****************************************  This is a scatter graph  ****************************************

dataframe["Strength_Gain"] = dataframe["Strength_Gain"].str.replace("%","").astype(int)

for gender in dataframe["Gender"].unique():
    subset = dataframe[dataframe["Gender"] == gender]
    plt.scatter(subset["Age"], subset["Strength_Gain"], label=gender)

plt.legend()
plt.xlabel("Age")
plt.ylabel("Strength Gain (%)")
plt.title("Age vs Strength Gain by Gender")
plt.show()

# ****************************************  End  ****************************************


# ****************************************  This graph will show which gender gained how much weight and strength (total) ****************************************

result = dataframe.groupby("Gender")[["Initial_WT","Final_WT","Strength_Gain"]].sum()

result.plot(kind="line", marker="o")
plt.title("Total Gain by Gender")
plt.xlabel("\nGender")
plt.ylabel("\nTotal Increased Weight and Strength Gain")
plt.xticks(rotation=0)
plt.show()

# ****************************************  End  ****************************************


# ****************************************  This graph is showing which supplement is most effective  ****************************************

supplement_means = dataframe.groupby("Supplement")[["Initial_WT","Final_WT"]].mean()
supplement_means.plot(kind="bar")
plt.title("Average Initial and Final Weight by Supplement")
plt.xlabel("\nSupplement")
plt.ylabel("\nAverage Weight")
plt.xticks(rotation=30)
plt.show()

# ****************************************  End  ****************************************

# ****************************************  This graph is visualizing classified Primary benefit on the basis of supplement  ****************************************

supplement_category_primary_benefit = dataframe.groupby(["Supplement", "Primary_Benefit"]).size().reset_index(name="Count")

sns.barplot(
    data = supplement_category_primary_benefit,
    x = 'Supplement',
    y = 'Count',
    hue = "Primary_Benefit"
)

plt.title("Number of People in each Supplement Category by Primary Benefit")
plt.xlabel("\nSupplement")
plt.ylabel("\nNo. of People")
plt.tight_layout()
plt.show()

# ****************************************  End  ****************************************


''' In this project I have analyzed the which supplement is most effective and which 
    age category is more likely to take supplements. 
    I have also analyzed the primary benefit of taking supplements and how many people are 
    in each primary benefit category. I have also analyzed the strength gain and weight gain of people
    who took supplements on the basis of gender. I have visualized the the filtered information from
    the dataset using bar graphs, line graphs and scatter plots.
'''
