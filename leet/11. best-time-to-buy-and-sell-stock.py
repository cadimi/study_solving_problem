"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Input
prices = [7,1,5,3,6,4]
prices = [2, 7, 1]

Output: 5
"""
import sys

prices = [7, 1, 5, 3, 6, 4]

profit = 0
min_price = sys.maxsize

# 최소값과 최대값 계속 갱신
for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

print(profit)

