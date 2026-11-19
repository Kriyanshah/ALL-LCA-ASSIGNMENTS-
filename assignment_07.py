import pandas as pd
#Step : 1 : read the file
df = pd.read_csv("C:/Users/kriya/Downloads/Titanic-Dataset.csv")

print(df)

import matplotlib.pyplot as plt
# count passengers in each class
counts = df["Pclass"].value_counts().sort_index()

# plot the bar graph 
plt.bar(counts.index, counts.values)

# Add labels and title 
plt.xlabel("Passenger Class")
plt.ylabel("Number of passengers")
plt.title("Number of passengers in each class")
plt.xticks([1,2,3])

# display the graph
plt.show()



#2
counts = df.groupby(["Survived", "Sex"]).size().unstack()
print(counts)
counts.plot(kind="bar")

plt.xlabel("Survived status")
plt.ylabel("Number of passengers")
plt.title("Titanic survival by gender")
plt.xticks([0, 1], ["Not Survived", "Survived"], rotation=0)

plt.show()




# scatter plot of [Age vs Fare], [Pclass vs Fare], [Pclass vs age]

data = df.dropna(subset=["Age", "Fare"])

# create scatter plot
plt.scatter(data["Age"], data["Fare"])
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Scatter plot of Age vs Fare")

# display graph
plt.show()



# A few passengers paid exceptionally high fares compared with most passengers

# remove missing values
data = df.dropna(subset=["Pclass", "Fare"])

# create scatter plot
plt.scatter(data["Pclass"], data["Fare"])

# add lables and titles
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.title("Scatter plot of Passenger Class vs Fare")

plt.xticks([1, 2, 3])
plt.grid(True)
plt.show()

# calculate the average fare for each passenger class
avg_fare = df.groupby("Pclass")["Fare"].mean()
# draw line graph
plt.plot(avg_fare.index, avg_fare.values, marker = "o")

# Add labels and title 
plt.xlabel("Passenger class")
plt.ylabel("Average fare")
plt.title("Average fare by passenger class")

plt.xticks([1,2,3])
plt.grid(True)

plt.show()