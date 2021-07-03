# abby chang

# input
# 有六行input，一行一個數字
adult_num = int(input())  # 全票數量
adult_price = int(input())  # 全票售價
student_num = int(input())  # 學生票數量
student_price = int(input())  # 學生票售價
money = int(input())  # 給付櫃台的金額
num_rst = int(input())  # 票券總張數限制
ttl_num = adult_num + student_num  # 票券總張數
remaining_num = num_rst - ttl_num  # 尚可購買的張數
ttl_price = adult_num * adult_price + student_num * student_price  # 總應付金額
remaining_money = money - ttl_price  # 櫃台找回來的錢

if ttl_num > num_rst:         # 假設票數大於票數限制
    final_num = -1
else:
    final_num = remaining_num   # 假設票數小於票數限制

if money < ttl_price:         # 假設錢不夠
    final_money = -2
else:                         # 假設錢夠
    final_money = "$" + str(remaining_money)

# output
print(final_num, final_money, sep=",")
