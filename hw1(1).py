# abby chang

# input
# 有五行input，一行一個數字
adult_num = int(input())  # 全票數量
adult_price = int(input())  # 全票售價
student_num = int(input())  # 學生票數量
student_price = int(input())  # 學生票售價
money = int(input())  # 給付櫃台的金額
ttl_price = adult_num * adult_price + student_num * student_price  # 總應付金額
remaining = money - ttl_price  # 櫃台找回來的錢

# output
if money < ttl_price:         # 假設錢不夠
    print("-1")
else:                          # 假設錢夠
    print("$" + str(remaining))
