import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from dotenv import load_dotenv
load_dotenv()
import os

my_email = os.environ.get("my_email")
port = os.environ.get("port")
password = os.environ.get("password")

headers = {
    "Accept-Language": "ru",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15"
}

url = "https://www.amazon.com/Black-Common-Outdoor-Session5-DBPOWER/dp/B00PLBXUMS/ref=sr_1_39?crid=2CW7BHE3XDQDT&keywords=gopro+kit&qid=1664195070&sprefix=gopro+ki%2Caps%2C286&sr=8-39"

response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
price = soup.find(name="span", class_="a-offscreen").getText()

if price.strip("$") <= 35:
    with smtplib.SMTP("smtp.gmail.com", port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=os.environ.get("to_addr"),
                            msg=f"Subject:Price Alert \n\n Urgent! The cost is {price} now\nTap the link:{url}")