import pandas as pd

#Create a dataframe based on a csv on my local
white_h_salary = pd.read_csv('/Users/marcellodamore/desktop/2010_Report_to_Congress_on_White_House_Staff.csv')

#Print the dataset
print(white_h_salary)

#Print details of dataframe
print(white_h_salary['Pay Basis'].describe())