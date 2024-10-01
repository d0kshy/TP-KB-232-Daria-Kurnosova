import requests

def getExchRate(currency_code):
    response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
    rates = response.json()
    for rate in rates:
        if rate['cc'] == currency_code:  # Find the exchange rate for the given currency
                    return rate['rate']

def convtoUAH(amount, currencyCode):
    exchangeRate = getExchRate(currencyCode)
    return amount * exchangeRate

amount = int(input("\nEnter the amount: "))
currencyCode = input("Enter the currency [EUR euro USD dollars PLN zloty]\nYour choice: ").upper()

finalRes = convtoUAH(amount, currencyCode)

print(f"{finalRes} UAH")

