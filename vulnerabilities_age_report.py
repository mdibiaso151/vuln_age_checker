import pandas as pd
from datetime import datetime, timedelta

# read in the xlsx file and store it in a DataFrame
df = pd.read_excel("combined.xlsx",engine='openpyxl')

# convert the 'Discovered Date' column to a datetime object
df['Discovered Date'] = pd.to_datetime(df['Discovered Date'])

# calculate the current date and the 45 and 90 day thresholds
now = datetime.now()
forty_five_days_ago = now - timedelta(days=45)
ninety_days_ago = now - timedelta(days=90)

# create a DataFrame for the vulnerabilities discovered more than 45 days ago
df_45 = df[(df['Discovered Date'] <= forty_five_days_ago)]

# create a DataFrame for the vulnerabilities discovered more than 90 days ago
df_90 = df[(df['Discovered Date'] <= ninety_days_ago)]

# Write the two dataframes to a new xlsx file, with separate sheets
with pd.ExcelWriter('vulnerabilities_age.xlsx') as writer:
    df_45.to_excel(writer, sheet_name='greater_than_45_days_old', index=False)
    df_90.to_excel(writer, sheet_name='greater_than_90_days_old', index=False)