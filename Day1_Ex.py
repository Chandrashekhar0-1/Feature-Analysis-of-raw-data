import pandas as pd
# Load the the titanic dataset
url= "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)
# Display data set information
#print("data set info:\n " )
#print(df.info())

# Display the first few rows of the dataset

#print("\n Data set Preview:\n")
#print(df.head())

#saperate the features
categorical_features = df.select_dtypes(include=['object']).columns
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns

print("\n Categorical Features:\n", categorical_features.tolist())
print("\n Numerical Features:\n", numerical_features.tolist())

# Display categorical features
print("\n Categorical Data features:\n")
for column in categorical_features:
    print(f"{column}:\n", df[column].value_counts(), "\n")

# Display numerical features
print("\n Numerical Data features:\n")
print(df[numerical_features].describe())