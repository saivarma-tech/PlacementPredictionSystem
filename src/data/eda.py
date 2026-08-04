from src.data.load_data import load_data
import matplotlib.pyplot as plt
def basic_eda(df):
    print("First five rows")
    print(df.head())
    print("Last five rows:")
    print(df.tail())
    print("25 to 35 rows:")
    print(df.iloc[25:36])
    print("Sample of 10 records:")
    print(df.sample(10))
    print("data types")
    print(df.dtypes)
    print(df)
    print('complete information')
    print(df["PlacementStatus"].value_counts())
    print(df.info())
    count = df["PlacementStatus"].value_counts()
    plt.figure(figsize = (6,5))
    plt.bar(count.index, count.values)
    plt.title("Distribution of Placement Status")
    plt.xlabel("Placement Status")
    plt.ylabel("Count")
    plt.savefig(r"C:\\Users\\svmah\\PycharmProjects\\PythonProject4\\PlacementPredictionSystem\\results\\placement_status.png")
    plt.show()

def univariate(df):
    plt.figure(figsize = (6,5))
    plt.hist(df["CGPA"],bins=10)
    plt.title("Histogram of CGPA")
    plt.xlabel("CGPA")
    plt.ylabel("Frequency")
    plt.savefig(r"C:\\Users\\svmah\\PycharmProjects\\PythonProject4\\PlacementPredictionSystem\\results\\CGPA_hist.png")
    plt.show()
    


if __name__ == "__main__":
    df = load_data()
    basic_eda(df)
    univariate(df)

