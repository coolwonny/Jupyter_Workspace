# grocery = ["Water", "Butter", "Eggs", "Apples", "Cinnamon", "Sugar", "Milk"]
# print(f"The first two items: {grocery[:2]}")
# print(f"The last five items: {grocery[-5:]}")
# print(f"Every other items: {grocery[1::2]}")
# grocery.append("flour")

# grocery[3] = "Gala Apples"

# print(f"The total number of items: {len(grocery)}")
# grocery.pop()
# print(grocery)
# grocery.append("Cream")
# del grocery[2]
# print(grocery)

# print(f"Index of Gala Apples is {grocery.index("Gala Apples")}")

# trading_pnl = [ -224,  352, 252, 354, -544,
#                 -650,   56, 123, -43,  254,
#                  325, -123,  47, 321,  123,
#                  133, -151, 613, 232, -311 ]

# total = 0
# count = 0
# average = 0
# minimum = 0
# maximum = 0

# profitable_days = []
# unprofitable_days = []

# for x in trading_pnl:
#     total += x
#     count += 1
#     if minimum == 0:
#         minimum = x
#     elif x < minimum:
#         minimum = x
#     elif x > maximum:
#         maximum = x
    
#     if x > 0:
#         profitable_days.append(x)
#     elif x <= 0:
#         unprofitable_days.append(x)

# average = total / count

# Percentage_profitable = round((len(profitable_days)) / count * 100, 2)
# precentage_unprofitable = 100 - Percentage_profitable

# print(f"Number of total trading days: {count}")
# print(f"Total profits and losses: {total}")
# print(f"Daily average profit and loss: {average}")
# print(f"Worst loss: {minimum}")
# print(f"Best gain: {maximum}")
# print(f"Number of profitable days: {len(profitable_days)}")
# print(f"Number of unprofitable days: {len(unprofitable_days)}")
# print(f"Percentage of profitable days: {Percentage_profitable}%")
# print(f"Percentage of unprofitable days: {precentage_unprofitable}%")
# print(f"Profitable days: {profitable_days}")
# print(f"Unprofitable days: {unprofitable_days}")

      
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

banks["Citigroup"] = 170
banks["American Express"] = 33
del banks["Wachovia"]
print(banks)

total = 0
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

for x, y in banks.items():
    total += y
    count += 1
    if minimum == 0:
       minimum = y
       minimum_key = x
    print(minimum_key)

    elif y < minimum:
        y = minimum 
        x = minimum_key 
    elif y > maximum:
        y = maximum 
        x = maximum_key
print(maximum_key)
#     if y >= 300:
#         mega_cap.append(x)
#     elif y >= 10:
#         large_cap.append(x)
#     elif y >= 2:
#         mid_cap.append(x)
#     elif y >= 0.3:
#         small_cap.append(x)

# average = total / count

# print(f"Total market cap: {total}")
# print(f"Total number of banks: {count}")
# print(f"Average market cap: {average}")
# print(f"largest bank: {maximum_key}")
# print(f"smallest bank: {minimum_key}")
# print()
# print(f"Mega Cap banks: {mega_cap}")
# print(f"Large cap: {large_cap}")
# print(f"mid cap: {mid_cap}")
# print(f"small cap:{small_cap}")
