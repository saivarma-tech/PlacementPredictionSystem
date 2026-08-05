from src.data.load_data import load_data
def basic_eda(df):
    print("First five rows")
    print(df.head())
    print("Last five rows:")
    print(df.tail())
    print("25 to 35 rows:")
    print(df.iloc[25:36])
    print("Sample of 10 records:")
    print(df.sample(10))
    print("Sample of 25 records:")
    print(df.sample(25))
from src.data.load_data import load_data
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def basic_ede(df):
    print(df.head())
    print("first 5 rows")
    print(df.head())
    print("last 5 rows")
    print(df.tail())
    print("print 25 to 35 rows")
    print(df.iloc[25:36])
    print(" print coloumn names")
    print(df.columns)
    print("datatypes")
    print(df.dtypes)
    print("Complete Information")
    print(df.info())
    print("no of null values")
    missing=df.isnull().sum()
    print(missing[missing > 0])
    print("no of duplicate records")
    print(df.duplicated().sum())
    print("Target variable status")
    count=df["PlacementStatus"].value_counts()
    plt.figure(figsize = (6,5))
    plt.bar(count.index,count.values)


    plt.xlabel("Placement Status")
    plt.ylabel("Number of Records")
    plt.savefig(r"C:/Users/sjaga/PycharmProjects/PythonProject3/PlacementPredictionSystem/results/placement_status_bar.png")
    plt.show()

def univariate(df):
    plt.figure(figsize = (6,5))
    plt.hist(df["CGPA"],bins=10)
    plt.title("Histogram of CGPA")
    plt.xlabel("CGPA")
    plt.ylabel("Frequency")
    plt.savefig(r"C:\Users\sjaga\PycharmProjects\PythonProject3\PlacementPredictionSystem\results\CGPA_hist.png")
    plt.show()
    gendercount = df["Gender"].value_counts()
    plt.figure(figsize=(6, 5))
    plt.pie(gendercount, labels=gendercount.index, autopct="%1.1f%%", startangle=90)
    plt.title("Gender Distribution Pie Chart")
    plt.savefig(r"C:\Users\sjaga\PycharmProjects\PythonProject3\PlacementPredictionSystem\results\gender_pie.png")
    plt.show()

def bivariate(df):
    plt.figure(figsize = (6,5))
    placed=df[["PlacementStatus"]==1]["CGPA"]
    notplaced=df[["PlacementStatus"]==0]["CGPA"]
    plt.boxplot([placed,notplaced],label=["placed","notplaced"])
    plt.title("CGPA vs Placements")
    plt.xlabel("Placement Status")
    plt.ylabel("CGPA")
    plt.scatter(df["CGPA"],df["AptitudeTestScore"])
    plt.title("CGPA vs Aptitude Test Score")
    plt.xlabel("CGPA")
    plt.ylabel("Aptitude Test Score")
    plt.savefig(r"C:\Users\sjaga\PycharmProjects\PythonProject3\PlacementPredictionSystem\results\cgpa_aptitude_scatter.png")
    plt.show()
    plt.close()

def multivariate(df):
    data = df[["CGPA", "AptitudeTestScore","PlacementStatus"]]
    correlation = data.corr()
    plt.figure(figsize=(6, 5))
    sns.heatmap(correlation,
                annot=True,
                cmap="coolwarm",
                fmt=".2f"
    )
    plt.title("Correlation HeatMap")
    plt.savefig(r"C:\Users\sjaga\PycharmProjects\PythonProject3\PlacementPredictionSystem\results\heatmap.png")
    plt.show()
    plt.close()

if __name__ == "__main__":
    df=load_data()
    #basic_ede(df)
    univariate(df)
    bivariate(df)
    multivariate(df)