import pandas as pd

# Read the CSV file
df = pd.read_csv('tackoverflow_qa.csv')

# Convert creationdate to datetime format
df['creationdate'] = pd.to_datetime(df['creationdate'])

# 1. All questions created before 2014
before_2014 = df[df['creationdate'] < '2014-01-01']

# 2. All questions with a score greater than 50
score_gt_50 = df[df['score'] > 50]

# 3. All questions with a score between 50 and 100 (inclusive)
score_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]

# 4. All questions answered by Scott Boston
answered_by_scott = df[df['ans_name'] == 'Scott Boston']

# 5. All questions answered by the following 5 users
users_list = ['User1', 'User2', 'User3', 'User4', 'User5']  # replace with actual usernames
answered_by_5_users = df[df['ans_name'].isin(users_list)]

# 6. Questions created between March 2014 and October 2014,
#    answered by Unutbu, and with a score less than 5
march_to_oct_unutbu = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'unutbu') &
    (df['score'] < 5)
]

# 7. Questions with a score between 5 and 10 OR a view count greater than 10,000
score_or_views = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) |
    (df['viewcount'] > 10000)
]

# 8. All questions NOT answered by Scott Boston
not_answered_by_scott = df[df['ans_name'] != 'Scott Boston']

# Example: print first few rows of the first filter
print(before_2014.head())

import pandas as pd

# Load dataset
titanic_df = pd.read_csv("titanic.csv")

# 1. Female Passengers in Class 1 with Ages between 20 and 30
female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'] >= 20) &
    (titanic_df['Age'] <= 30)
]

# 2. Passengers Who Paid More than $100
fare_gt_100 = titanic_df[titanic_df['Fare'] > 100]

# 3. Passengers Who Survived and Were Alone (no siblings/spouses and no parents/children)
survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]

# 4. Passengers Embarked from 'C' and Paid More Than $50
embarked_c_fare_gt_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]

# 5. Passengers with Siblings/Spouses AND Parents/Children
sibsp_and_parch = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]

# 6. Passengers Aged 15 or Younger Who Didn't Survive
age_le15_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]

# 7. Passengers with Cabins and Fare Greater Than $200
cabin_and_fare_gt_200 = titanic_df[
    titanic_df['Cabin'].notna() &
    (titanic_df['Fare'] > 200)
]

# 8. Passengers with Odd-Numbered Passenger IDs
odd_passenger_id = titanic_df[titanic_df['PassengerId'] % 2 == 1]

# 9. Passengers with Unique Ticket Numbers
unique_ticket = titanic_df[
    ~titanic_df['Ticket'].duplicated(keep=False)
]

# 10. Passengers with 'Miss' in Their Name and Were in Class 1
miss_in_name_class1 = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Sex'] == 'female')
]

# Example: Show results for one filter
print(female_class1_20_30)
