import pandas as pd
#Step : 1 : read the file
df = pd.read_csv("C:/Users/kriya/Downloads/Titanic-Dataset.csv")

# Step : 2 : dataset dimensions
print("Shape:")
print(df.shape)

# Step : 3 :column names and data types
print("\ncolumns:")
print(df.columns)

# Step : 4 : data types
print("\nData types:")
print(df.dtypes)

# Step : 5 : statistical summary
print("\nSatistical summary: ")
print(df.describe())

# step : 6 : display the first five rows
print("First five rows:")
print(df.head())

# step : 7 : display the last five rows
print("\nlast five rows")
print(df.tail())

# step : 8 : display dataset information
print("\nData info:")
print(df.info())

# step : 9 : display passenger name
print("\nPassenger name:")
print(df["Name"].head())

# step : 10 : count passenger by class
print("\nPassenger by gender:")
print(df["Pclass"].value_counts())

# step : 11 : calculate avg age 
print("\nAvg age:")
print(df["Age"].mean())

# step : 12 : highest fare
print("\nHighest fare :")
print(df["Fare"].max())

# step : 13 : avg fare 
print("\nAverage fare:")
print(df["Fare"].mean())

#step : 14 : delete columns
df = df.drop(['Cabin', 'Embarked'], axis=1)
        #             OR
    # df = df.drop(columns= ('cabin', 'Embarked'))
print(df)

#step : 15 : filter passengers older than 60
print("\nPassenger older than 60:")
print(df[df["Age"]>60][["Name", "Age", "Sex"]])

#step : 16 : display passengers who survived
print("\nPassengers who survived:")
print(df[df["Survived"]==1][["Name", "Sex", "Age"]].head())

# step : 17 : Count survivors and non survivors
print("\nSurvival counts:")
print(df["Survived"].value_counts())

# step : 18 : calculate survival rate by gender
print("\nSurvival rate by gender:")
print(df.groupby("Sex")["Survived"].mean()*100)

# step : 19 : sort passengers by fare 
print("\nTop 10 Highest fares: ")
print(
    df.sort_values("Fare", ascending=False)
    [["Name", "Fare"]].head(10)
)
