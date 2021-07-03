# abby chang

kg = int(input()) # 欲買公斤數
kg1 = int(input()) # 級距1公斤數
price1 = int(input())# 級距1價錢
kg2 = int(input()) # 級距2公斤數
price2 = int(input()) # 級距2價錢
kg3 = int(input()) # 級距3公斤數
price3 = int(input()) # 級距3價錢

if kg <= kg1: #total
 total = kg * price1
if kg1 < kg <= kg2:
 total = kg1 * price1 + (kg - kg1) * price2
if kg2 < kg <= kg3:
 total = kg1 * price1 + (kg2 - kg1) * price2 + (kg - kg2) * price3

#output
print(total) 