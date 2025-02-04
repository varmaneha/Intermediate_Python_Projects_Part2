import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "r43754rguqdh2rt93" #Your API Key
NEWS_API_KEY = "bcdfewiufclkoeckb" #Your API Key
TWILIO_SID = "nsckdbvsbscvksnlsd"
TWILIO_AUTH_TOKEN = "iubkfykfvj,hdugivsbzb"


stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(data_list)



day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)


difference = float(yesterday_closing_price - day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "▲"
else:
    up_down = "▼"


diff_percent = round(difference / float(yesterday_closing_price)) * 100
print(diff_percent)

if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        
    }
    
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    
    
    client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+51473252885",
            to="45825235925"
        
    )
