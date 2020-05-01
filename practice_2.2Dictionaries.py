# # -*- coding: utf-8 -*-
# """
# Instructor Demo: Dicts.
# This script showcases basic operations of Python Dicts.
# """

#   # Initialize a dictionary containing top traders for each month in 2019
# top_traders_2019 = {
#     "january" : "Karen",
#     "february" : "Harold",
#     "march" : "Sam"
# }

# print()
# print(f"Dictionary: {top_traders_2019}")
# print()

# # Initialize a dictionary
# trading_pnl = {
#     "title": "Trading Log",
#     "03-18-2019": -224,
#     "03-19-2019": 352,
#     "03-20-2019": 252,
#     "03-21-2019": 354,
#     "03-22-2019": -544,
#     "03-23-2019": -650,
#     "03-24-2019": 56,
#     "03-25-2019": 123,
#     "03-26-2019": -43,
#     "03-27-2019": 254,
#     "03-28-2019": 325,
#     "03-29-2019": -123,
#     "03-30-2019": 47,
#     "03-31-2019": 321,
#     "04-01-2019": 123,
#     "04-02-2019": 133,
#     "04-03-2019": -151,
#     "04-04-2019": 613,
#     "04-05-2019": 232,
#     "04-06-2019": -311
# }

# # Print out dictionary, initial print() to serve as spacing between command line input
# print()
# print(f"Dictionary: {trading_pnl}")
# print()

# # Print out specific value of a key
# print(f"03-31-2019: {trading_pnl['03-31-2019']}")
# print()

# # Add a new key-value pair
# trading_pnl["04-07-2019"] = 413
# print(trading_pnl)
# print()

# # Modify a key value
# trading_pnl["04-07-2019"] = 542
# print(trading_pnl)
# print()

# # Delete a key-value pair
# del trading_pnl["04-07-2019"]
# print(trading_pnl)
# print()

# # Check if key exists
# if "04-03-2019" in trading_pnl:
#     print("Yes, '04-03-2019' is one of the keys in the trading_pnl dictionary")
# print()

# # Print out dict keys via a for loop
# for key in trading_pnl:
#     print(f"Key: {key}")
# print()

# # Print out dict values
# for key in trading_pnl:
#     print(f"Value: {trading_pnl[key]}")
# print()

# # Print out dict key-value pairs
# for key, value in trading_pnl.items():
#     print(f"Key: {key} Value: {value}")
# print()

# -*- coding: utf-8 -*-
"""
Student Activity: Market Capitalization.

This script showcases the use of Python Dicts to determine the
bank names associated with the corresponding market cap ranges.
"""

# Banks and Market Caps
#-----------------------
# JP Morgan Chase: 327
# Bank of America: 302
# Citigroup: 173
# Wells Fargo: 273
# Goldman Sachs: 87
# Morgan Stanley: 72
# U.S. Bancorp: 83
# TD Bank: 108
# PNC Financial Services: 67
# Capital One: 47
# FNB Corporation: 4
# First Hawaiian Bank: 3
# Ally Financial: 12
# Wachovia: 145
# Republic Bancorp: .97

# @TODO: Initialize a dictionary of banks and market caps (in billions)


# # @TODO: Change the market cap for 'Citigroup'
# banks["Citigroup"] = 185

# # @TODO: Add a new bank and market cap pair
# banks["USAA"] = 13


# # @TODO: Remove a bank from the dictionary
# del banks["USAA"]


# # @TODO: Print the modified dictionary
# banks["Citigroup"] = 170
# banks["American Express"] = 33
# del banks["Wachovia"]


# Challenge
# Group banks by their corresponding market capitalization tier.
# Iterate over the key-value pairs in the banks dictionary and calculate the following:

# Total market capitalization
# Total number of banks
# Average market capitalization
# Largest bank
# Smallest bank

# Use an if-else statement and lists to compare and group banks by their corresponding market capitalization: mega-cap, large-cap, mid-cap, and small-cap.

# mega-cap: Market capitalization greater than or equal to $300 billion.
# large-cap: Market capitalization greater than or equal to $10 billion and less than $300 billion.
# mid-cap: Market capitalization greater than or equal to $2 and less than $10 billion.
# small-cap: Market capitalization greater than or equal to $300 million and less than $2 billion.

banks = {
    "JP Morgan Chase": 327,
    "Bank of America": 302,
    "Citigroup": 173,
    "Wells Fargo": 273,
    "Goldman Sachs": 87,
    "Morgan Stanley": 72,
    "U.S. Bancorp": 83,
    "TD Bank": 108,
    "PNC Financial Services": 67,
    "Capital One": 47,
    "FNB Corporation": 4,
    "First Hawaiian Bank": 3,
    "Ally Financial": 12,
    "Wachovia": 145,
    "Republic Bancorp": .97
}

total = 0
total_market_cap = 0
count = 0
average = 0
minimum = 0
maximum = 0
minimum_key = ""
maximum_key = ""

mega_cap = []
large_cap = []
mid_cap = []
small_cap = []

for bank_name, market_cap in banks.items():
    total_market_cap += int(market_cap)
    count += 1
    if minimum == 0:
        minimum = market_cap
        minimum_key = bank_name
    elif market_cap < minimum:
        minimum = market_cap
        minimum_key = bank_name
    elif market_cap > maximum:
        maximum = market_cap
        maximum_key = bank_name

    if market_cap >= 300:
       mega_cap.append(bank_name)
    elif market_cap >= 10:
        large_cap.append(bank_name)
    elif  market_cap >= 2:
        mid_cap.append(bank_name)
    elif market_cap >= 0.3:
        small_cap.append(bank_name)

# for key in banks:
#     x = banks[key]
#     total_market_cap += x
#     count += 1
    
#     if minimum == 0:
#         minimum = x
#         minimum_key = key
#     elif x < minimum:
#         minimum = x
#         minimum_key = key
#     elif x > maximum:
#         maximum = x
#         maximum_key = key

#     if x >= 300:
#        mega_cap.append(key)
#     elif x >= 10:
#         large_cap.append(key)
#     elif  x >= 2:
#         mid_cap.append(key)
#     elif x >= 0.3:
#         small_cap.append(key)



average =  round(total_market_cap / count, 2)

print(f"Total Market Capitalization: {total_market_cap}")
print(f"Total Number of Banks: {count}")
print(f"Average Market Capitalization: {average}")
print(f"Largest Bank: {maximum_key}")
print(f"Smallest Bank: {minimum_key}")
print(f"Mega Cap Banks: {mega_cap}")
print(f"Large Cap Banks: {large_cap}")
print(f"Mid Cap Banks: {mid_cap}")
print(f"Small Cap Banks: {small_cap}")



