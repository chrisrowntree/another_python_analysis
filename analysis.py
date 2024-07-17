import pandas as pd

# Load the first Excel file
df1 = pd.read_excel('Big MIR Vessels.xlsx', sheet_name='High plan vessels')

# Load the second Excel file
df2 = pd.read_excel('MIR Uplink.xlsx')

# Determine the type of join you need: 'inner', 'outer', 'left', 'right'
# Here, we use 'inner' join on a common column 'key'

merged_df = pd.merge(df1, df2, on='siteId', how='inner')

# Save the merged dataframe to a new Excel file
merged_df.to_excel('merged_file.xlsx', index=False)

# Print the first 20 rows of the merged dataframe
print(merged_df.head(20))

print("Files have been merged and saved to 'merged_file.xlsx'")