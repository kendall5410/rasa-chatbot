import requests
from bs4 import BeautifulSoup

def scrape_drift():
    url = "https://www.drift.com/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract relevant data from the website (e.g., company info, news).
        # For simplicity, let's just return a sample data.
        return ["Sample data from drift.com."]
    else:
        print("Failed to retrieve data from drift.com.")
        return []
