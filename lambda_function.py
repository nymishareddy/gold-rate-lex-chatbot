import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    url = 'https://www.bankbazaar.com/gold-rate.html'
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    hyderabad_rate_24k = None

    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:
            cols = row.find_all('td')
            if len(cols) >= 3:
                city = cols[0].get_text(strip=True).lower()
                rate_24k = cols[2].get_text(strip=True).split('(')[0].strip()
                if city == 'hyderabad':
                    hyderabad_rate_24k = rate_24k
                    break

    if hyderabad_rate_24k:
        message = f"The current 24K gold rate in Hyderabad is {hyderabad_rate_24k}."
    else:
        message = "Sorry, I couldn’t find the gold rate for Hyderabad."

    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": "GetGoldRate",
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": message
            }
        ]
    }
