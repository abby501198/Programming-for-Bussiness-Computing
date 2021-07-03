# abby chang  '''有票數有逗號，沒票數沒逗號'''

# input
# 有六行input，一行一個數字
adult_num = int(input()) # 全票數量
adult_price = int(input()) # 全票售價
student_num = int(input()) # 學生票數量
student_price = int(input()) # 學生票售價
money = int(input()) # 給付櫃台的金額
num_rst = int(input()) #票券總張數限制

ttl_num = adult_num + student_num # 票券總張數
remaining_num = num_rst - ttl_num #尚可購買的張數
ttl_price = adult_num * adult_price + student_num * student_price # 總應付金額
remaining_money = money - ttl_price # 櫃台找回來的錢

if ttl_num <= num_rst:        
  if money >= ttl_price:      # 票夠且錢夠
    print(str(remaining_num) + "," + "$" + str(remaining_money))
  else:                       #票夠且錢不夠
    print(str(remaining_num) + ",") 
elif money >= ttl_price:      # 票不夠且錢夠
  print("$" + str(remaining_money))