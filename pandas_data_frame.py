import pandas as pd
import sqlite3
# data_frame = pd.read_csv('learninja/topics_backup.csv')
# print(data_frame.head(3))

con = sqlite3.connect("learninja/data.sqlite")
data_frame = pd.read_sql_query("SELECT * from topics", con)
course_list_unique = data_frame['course'].unique()
print(course_list_unique)
for course in course_list_unique:
    subject_list = data_frame[data_frame['course'] == course]
    subject_list_unique = subject_list['subject'].unique()
    print(f'{course}: {subject_list_unique}')
print(data_frame[['subject'][data_frame.course == 'Course 1']])
# Verify that result of SQL query is stored in the dataframe
# print(data_frame.head())
topic_list = data_frame[data_frame['subject'] == 'Subject 1']
print(topic_list)

print(subject_list)
con.close()
