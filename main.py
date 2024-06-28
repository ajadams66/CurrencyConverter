import currencyapicom

# Currency(country_code='THB', currency_amt='4,000', trans_code='USD')

country_code = input('What is the Country code you are transferrring from?').upper()
how_much = input('How much do you want to convert')
new_code = input('Which currency will you be changing the currency to?').upper()
# time.sleep(2)

my_key = 'API-KEY'
client = currencyapicom.Client(my_key)
result = client.latest(country_code, currencies=[new_code])
foreign_currency = result['data'][new_code]['value']
new_amount = (float(how_much) * foreign_currency)
new_amount = round(new_amount,2)
print(f'{country_code}: {how_much} \n {new_code}: {new_amount} ')
