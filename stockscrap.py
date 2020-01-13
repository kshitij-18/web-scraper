import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

res = requests.get('https://www.equitymaster.com/share-price/GAIL/GAIL-532155/GAIL-Share-Price?utm_source=stock-quotes&utm_medium=website&utm_campaign=company-name&utm_content=stock-quotes')
soup = BeautifulSoup(res.text, 'html.parser')
gail_stock_price= float(soup.select('.c-yellow')[0].getText().replace('Price (Rs)',''))

def send_email(stock_price):
    email=EmailMessage()

    email['from'] = 'Kshitij Nath'
    email['to']='kshitijnath@gmail.com'
    email['subject']='Good time to invest in Gail'

    email.set_content(f'This is the right time to in Gail \n Stock Price of Rs{stock_price}')

    with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('kshitijnath@gmail.com','kshitij18!')
        smtp.send_message(email)
        print('sent successfully')

if gail_stock_price<115:
    send_email(gail_stock_price)
    print(f'Stock Price is {gail_stock_price}')