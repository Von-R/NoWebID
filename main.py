import requests
import pandas as pd

# Phase 1: Data collection from API 1 (Business Directory)
# Placeholder for API data
api1_data = [
    {"name": "Business 1", "phone": "1234567890"},
    {"name": "Business 2", "phone": "0987654321"}
]
# Uncomment below lines for actual API request
# url1 = 'https://api1-example.com/businesses'
# response1 = requests.get(url1)
# api1_data = response1.json()

# Phase 2: Data collection from API 2 (Social Media Data)
# Placeholder for API data
api2_data = [
    {"name": "Business 1", "social_media_followers": 200},
    {"name": "Business 2", "social_media_followers": 150}
]


# Uncomment below lines for actual API request
# url2 = 'https://api2-example.com/social_media_data'
# response2 = requests.get(url2)
# api2_data = response2.json()

# Phase 3: Check Website Presence
def check_website(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False


for business in api1_data:
    website_url = f"http://www.{business['name'].replace(' ', '').lower()}.com"
    business['has_website'] = check_website(website_url)

# Phase 4: Synthesize Data
df1 = pd.DataFrame(api1_data)
df2 = pd.DataFrame(api2_data)

# Merge data on the "name" column
df_merged = pd.merge(df1, df2, on="name", how="outer")

# Phase 5: Store Data in CSV
df_merged.to_csv('comprehensive_local_business_data.csv', index=False)
