import requests
from dotenv import load_dotenv
import os
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
load_dotenv(".env")
alphavantage_route = "https://www.alphavantage.co/query"
alphavantage_api_key = os.getenv("alphavantage_api_key")

parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "30min",
    "apikey": alphavantage_api_key
}

response = requests.get(alphavantage_route, params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
stock_time_series = data["Time Series (30min)"]
# print(stock_time_series)

# NASDAQ open at 9:30 am and closes at 4 pm
# but alphavantage works from 4:30 am to 8 pm

# Get today's date
today = dt.date.today()


# print("Today is: ", today)

# THE STOCK MARKET DOES NOT WORK ON SATURDAY AND SUNDAY AND OFTEN IS NOT
# UPDATED ON TIME TO COMPARE MONDAY AT THE END OF TUESDAY
def get_last_friday():
    now = dt.datetime.now()
    closest_friday = now + dt.timedelta(days=(4 - now.weekday()))
    return (closest_friday if closest_friday < now
            else closest_friday - dt.timedelta(days=7))


def get_last_thursday():
    now = dt.datetime.now()
    closest_friday = now + dt.timedelta(days=(3 - now.weekday()))
    return (closest_friday if closest_friday < now
            else closest_friday - dt.timedelta(days=7))


def find_percent_difference(a, b):
    return ((abs(a - b)) / ((a + b) / 2)) * 100


MONDAY = 1
TUESDAY = 2
SATURDAY = 6
SUNDAY = 7
current_weekday = dt.datetime.now().weekday()

if current_weekday == MONDAY or TUESDAY or SATURDAY or SUNDAY:
    print(
        "this program is a highly unstable experiment! it can only work on "
        "Wednesday, Thursday and Friday (you would otherwise be at a threat of becoming too rich - no problem)")
    # we swap the two days we compare to Thursday and Friday of last week
    print("...so we are doing it for the end of last week.")
    # Friday date
    yesterday = str(get_last_friday()).split(" ")[0]
    print("Yesterday (Friday) was: ", yesterday)

    # Thursday date
    day_before_yesterday = str(get_last_thursday()).split(" ")[0]
    print("The day before yesterday (Thursday) was: ", day_before_yesterday)
else:
    # Yesterday date
    yesterday = today - dt.timedelta(days=1)
    print("Yesterday was: ", yesterday)

    # The day before yesterday date
    day_before_yesterday = today - dt.timedelta(days=2)
    print("The day before yesterday was: ", day_before_yesterday)

string_start = f"{yesterday} 04:30:00"
string_end = f"{yesterday} 20:00:00"
stock_price_yesterday_start = stock_time_series[string_start]
stock_price_yesterday_end = stock_time_series[string_end]
# print(f"Yesterday start 4:30AM: {stock_price_yesterday_start}")
# print(f"Yesterday end 8PM: {stock_price_yesterday_end}")
cost_yesterday_start_average = (float(stock_price_yesterday_start['3. low']) + float(
    stock_price_yesterday_start['2. high'])) / 2
cost_yesterday_end_average = (float(stock_price_yesterday_end['3. low']) + float(
    stock_price_yesterday_end['2. high'])) / 2
cost_yesterday_average = (cost_yesterday_start_average + cost_yesterday_end_average) / 2
print(f"average stock cost yesterday: {cost_yesterday_average}")

string_start = f"{day_before_yesterday} 04:30:00"
string_end = f"{day_before_yesterday} 20:00:00"
# print(stock_time_series["2023-02-13 05:30:00"])
stock_price_before_yesterday_start = stock_time_series[string_start]
stock_price_before_yesterday_end = stock_time_series[string_end]
# print(f"Day before yesterday start 4:30AM: {stock_price_before_yesterday_start}")
# print(f"Day before yesterday end 8PM: {stock_price_before_yesterday_end}")
cost_before_yesterday_start_average = (float(stock_price_before_yesterday_start['3. low']) + float(
    stock_price_before_yesterday_start['2. high'])) / 2
cost_before_yesterday_end_average = (float(stock_price_before_yesterday_end['3. low']) + float(
    stock_price_before_yesterday_end['2. high'])) / 2
cost_before_yesterday_average = (cost_before_yesterday_start_average + cost_before_yesterday_end_average) / 2
print(f"average stock cost yesterday: {cost_before_yesterday_average}")

percent_difference = round(find_percent_difference(cost_before_yesterday_average, cost_yesterday_average), 2)
print(f"{percent_difference}% difference")

if percent_difference >= 5:
    print("THERE IS MORE THAN A 5% DIFFERENCE, LOOK INTO IT")
    # # STEP 2: Use https://newsapi.org
    # ^ this also has an api for python (but I'll go the response route)
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_route = "https://newsapi.org/v2/everything"
    news_api_key = os.getenv("newsapi_key")

    parameters = {
        "q": COMPANY_NAME,
        "from": str(today),
        "sortBy": "popularity",
        "apiKey": news_api_key
    }

    response = requests.get(news_route, params=parameters)
    response.raise_for_status()
    # pick an article to send (i just randomly pick the 3rd here)
    # possible out of range, but we're chilling
    data = response.json()['articles'][2]

    description = f"{COMPANY_NAME}: {percent_difference}% deviation"
    title = data['title']
    content = data['content'].split('[')[0]
    # print(f"Title: {title}")
    # print(f"Content: {content}")
    sms_body = f"{description}\n" \
               f"{title}\n" \
               f"{content}\n"

    # # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    trial_number = os.getenv("trial_number")
    my_number = os.getenv("my_number")
    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("auth_token")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=my_number,
        body=sms_body,
        from_=trial_number
    )
    print(message.sid)
    # Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
else:
    print("there seem to be no cash money opportunities for this stock, BUT NOT FOR ALL OF THEM - bet your house NOW")
