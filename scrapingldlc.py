import requests
from bs4 import BeautifulSoup
import smtplib

# My User Agent
User_agent = {
"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}

# Url du produit
URL = 'https://www.ldlc.com/fiche/PB00247997.html'


def prixldlc():


    page = requests.get(URL, User_agent)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Parser the html
    titre = soup.find('h1')
    prix = soup.find_all("div", class_="price")
    prix = prix[3].text
    prix_convert_euro = prix[:-3]
    prix_convert_centims = prix[-2:]
    prix = float(prix_convert_euro +'.'+ prix_convert_centims)
    print(prix)


    if prix < 170.00:
        send_email()

    print(titre.text)
    print(prix)


def send_email():


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Google app password : myaccount.google.com › apppasswords
    server.login('niicolaas67@gmail.com', 'rtiknaybvzcqjtud')

    sujet = 'LE PRIX EN BAISSE'
    corps = "VERIFIER LE LIEN https://www.ldlc.com/fiche/PB00247997.html"
    msg = f"Subject: {sujet}\n\n{corps}"
    # From / To / msg
    server.sendmail(
        "niicolaas67@gmail.com",
        "niicolaas67@yahoo.fr",
        msg
    )
    print("EMAIL ENVOYEE")

    server.quit()

prixldlc()


