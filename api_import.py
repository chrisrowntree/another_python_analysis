import requests
import pandas as pd

# URL to fetch posts data from JSONPlaceholder
url = 'https://jsonplaceholder.typicode.com/posts'

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    # Convert to DataFrame for better readability
    df = pd.DataFrame(data)
    # Display the first few records for a quick overview
    print(df.head(10))
    #save output to excel
    df.to_excel('api_output.xlsx', index=False)
    #Print success message
    print("Success!")
    
else:
    print("Failed to fetch data:", response.status_code)