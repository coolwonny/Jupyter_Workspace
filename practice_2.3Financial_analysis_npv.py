
import numpy_financial 

discount_rate = .1
cash_flows_conservative = [-1000, 400, 400, 400, 400]
cash_flows_neutral = [-1500, 600, 600, 600, 600]
cash_flows_aggressive = [-2250, 800, 800, 800, 800]

npv_dict = {}

npv_conservative = npf.npv(discount_rate, cash_flows_conservative)
npv_neutral = npf.npv(discount_rate, cash_flows_neutral)
npv_aggressive = npf.npv(discount_rate, cash_flows_aggressive)

print(npv_conservative)