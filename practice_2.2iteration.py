# count = 0
# total = 0
# average = 0
# minimum = 0
# maximum = 0

# cash_tips = [22, 10, 30, 45, 54, 60, 56]

# for tip in cash_tips:
#     total += tip
#     count += 1
#     if minimum == 0:
#         minimum = tip
#     elif tip < minimum:
#         minimum = tip
#     elif tip > maximum:
#         maximum = tip

# print(minimum, maximum) 
# average = round(total / count, 2)

# print("---------Summary Statistics----------")
# print(f"Number of Days: {count}")
# print(f"Total Tips: {total}")
# print(f"Daily Average: {average}")
# print(f"Least Amount of Tips: {minimum}")
# print(f"Maximum Amount of Tips: {maximum}")

# -*- coding: utf-8 -*-
"""
Student Do: Trading Log.

This script demonstrates how to perform basic analysis of trading profits/losses
over the course of a month (20 business days).
"""

# @TODO: Initialize the metric variables

count = 0
total = 0
average = 0
minimum = 0
maximum = 0

# @TODO: Initialize lists to hold profitable and unprofitable day profits/losses
profitable_day = []
unprofitable_day = []

# List of trading profits/losses
trading_pnl = [ -224,  352, 252, 354, -544,
                -650,   56, 123, -43,  254,
                 325, -123,  47, 321,  123,
                 133, -151, 613, 232, -311 ]

# @TODO: Iterate over each element of the list
for x in trading_pnl:
    total += x
    count += 1
    if minimum == 0:
       minimum = x
    elif x < minimum:
        minimum = x
    elif x > maximum:
        maximum = x

    # @TODO: Cumulatively sum up the total and count
    # @TODO: Write logic to determine minimum and maximum values
    # @TODO: Write logic to determine profitable vs. unprofitable days
    if x > 0:
        profitable_day.append(x)
    else: 
        unprofitable_day.append(x)


# @TODO: Calculate the average
average = round(total / count, 2)


# @TODO: Calculate count metrics
no_of_profitable_days = len(profitable_day)
no_of_unprofitable_days = len(unprofitable_day)

# @TODO: Calculate percentage metrics
percentage_profitable_days = no_of_profitable_days / count * 100
percentage_unprofitable_days = 100 - percentage_profitable_days

# @TODO: Print out the summary statistics

print("---------Summary Statistics----------")
print(f"Number of total trading days: {count}")
print(f"Total profits and losses: {total}")
print(f"Daily Average profit and losses: {average}")
print(f"Worst loss: {minimum}")
print(f"Best gain: {maximum}")
print("-------------------------------------")
print(f"The values of profitable days: {profitable_day}")
print(f"The values of Unprofitable days: {unprofitable_day}")
print("-------------------------------------")
print(f"Number of profitable days: {no_of_profitable_days}")
print(f"Number of unprofitable days: {no_of_unprofitable_days}")
print(f"Percentage of profitable days: {percentage_profitable_days}%")
print(f"Percentage of unprofitable days: {percentage_unprofitable_days}%")
