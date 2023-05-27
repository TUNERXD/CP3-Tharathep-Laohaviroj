# API import

from forex_python.bitcoin import BtcConverter
from forex_python.converter import CurrencyCodes
import datetime

# some API settings

btc_converter = BtcConverter()
currency_code = CurrencyCodes()

# date time input

print("This Program Calculate the Percentage of BTC Increasing or Decreasing")
print("---------- Information ----------", "\n")
print('* latest update date is 18/07/2010 - 10/07/2022')
print("- Please Enter The date XX/XX/XXXX")
print("- Please Enter The currency Ex. USD,EUR,THB, etc..", "\n")
print("---------- Input ----------", "\n")
start = input("Enter the start date: ")
end = input("Enter the end date  : ")
start_date = datetime.datetime.strptime(start, "%d/%m/%Y")
end_date = datetime.datetime.strptime(end, "%d/%m/%Y")

# time set 0

start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
end_date = end_date.replace(hour=0, minute=0, second=0, microsecond=0)

# currency input

currency = input("Enter the currency      : ").upper()
print("\n")

# get prices

start_price = btc_converter.get_previous_price(currency, start_date)
end_price = btc_converter.get_previous_price(currency, end_date)

if start_price is None or end_price is None:
    print("Date input is out of range")
    print("please try again")
    print('* latest update date is 18/07/2010 - 10/07/2022', "\n")
    print("End Of Program")
else:
    print("---------- Prices ----------")
    print("BTC price start date: ", btc_converter.get_previous_price(currency, start_date),
          currency_code.get_symbol(currency))
    print("BTC price end date  : ", btc_converter.get_previous_price(currency, end_date),
          currency_code.get_symbol(currency), "\n")

    # Calculate increasing / decreasing percentage

    if start_price < end_price:
        increasing_percentage = round((((end_price - start_price) / start_price) * 100), 2)
        print("---------- Results ----------", "\n")
        print("from", start_date, "to", end_date)
        print("BTC price has increased by", "\n")
        print(increasing_percentage, "%", "\n")
        print("Note: percentage may vary due to different currency", "\n")
        print("End Of Program")

    elif start_price > end_price:
        decreasing_percentage = round((((start_price - end_price) / start_price) * 100), 2)
        print("---------- Results ----------", "\n")
        print("from", start_date, "to", end_date)
        print("BTC price has decreased by", "\n")
        print(decreasing_percentage, "%", "\n")
        print("Note: percentage may vary due to different currency", "\n")
        print("End Of Program")

    else:
        print("The price is stable", "\n")
        print("End Of Program")
