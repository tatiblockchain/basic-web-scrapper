import requests
from bs4 import BeautifulSoup

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


headers =  {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}



url = "https://vc4a.com/programs/"
r = requests.get(url, headers=headers)
c = r.content
soup = BeautifulSoup(c, "html.parser")


li_interest = soup.find_all("li", {"class": "partners-list__item partners-list__item-program partners-list__item--premium partners-list__item--featured"})
h3_interest = li_interest[0].find("h3")


title_option1 = h3_interest.find("a").text
link_interest = h3_interest.find("a")['href']
title_option2 = h3_interest.find("a")['title']

url2 = "https://vc4a.com" + link_interest
r2 = requests.get(url2, headers=headers)
c2 = r2.content
soup2 = BeautifulSoup(c2, "html.parser")

tr_interest = soup2.find_all("tr")             
td_interest = tr_interest[0].find_all("td")

deadline = td_interest[1].text
td = tr_interest[3].find_all("td")[1]
website = td.find("a")['href']


def shortEmail():

    strFrom = 'enter-email-sender'
    strTo = 'enter-receiver'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = '👋 Apply for this Opportunity Now'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'We found an amazing opportunity'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    altText = """
        Bertha,

        WE found this amazing opportunity.
        Name: {}
        Website URL: {}
        Application Closign date: {}



        Kind regards,
        Webmaster

    """.format(title_option2, website, deadline)

    msgText = MIMEText(altText)
    msgAlternative.attach(msgText)


    smtp = smtplib.SMTP()
    smtp.connect('enter-email-host')
    smtp.login('enter-username-email', 'enter-password')
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()



shortEmail()

