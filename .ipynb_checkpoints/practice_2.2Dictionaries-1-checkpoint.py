
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



