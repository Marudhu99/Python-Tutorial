import datetime

'''
%b - Month name short version: Dec
%B - Month name full version: December
%m - Month as a number 01-02

'''

current_date = datetime.date.today()
print("Current date:",current_date)

specific_date = datetime.date(2023,7,8)
print("Specific date:",specific_date)

#access different components of a date
year = specific_date.year
month = specific_date.month
day = specific_date.day
print("Year:",year,"Month:",month,"Day:",day)

#formatted date as a string
formatted_date = specific_date.strftime("%d-%b-%Y") # %b - onth name, short version - Dec
print("Formatted date:",formatted_date)

#parse a string into date object
date_string = "2023-07-08"
parse_date = datetime.datetime.strptime(date_string,"%Y-%m-%d").date()
print("Parse_date:",parse_date)

#perform arithmetic  operations with dates
future_date = specific_date + datetime.timedelta(days=10)
past_date = specific_date - datetime.timedelta(days=5)
print("Future date:",future_date)
print("Past date:",past_date)