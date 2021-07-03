# abby chang
num_of_products = int(input())  # 商品數量
product_set_str = input()   # 折價的編號
product_set_list = product_set_str.split(",")
product_price_str = input()     # 商品價錢
product_price_list = product_price_str.split(",")
product_that_purchased_str = input()    # 各商品的購買數量
product_that_purchased_list = product_that_purchased_str.split(",")

# 將list裡的值轉成int
for i in range(len(product_set_list)):  # 將各編號減1讓編號從0開始    # in list,there are all int.  
    product_set_list[i] = int(product_set_list[i]) - 1
for i in range(len(product_price_list)):
    product_price_list[i] = int(product_price_list[i])
for i in range(len(product_that_purchased_list)):
    product_that_purchased_list[i] = int(product_that_purchased_list[i])

# 算在set裡的購買數量
discountnum = []
for i in product_set_list:
    temp = product_that_purchased_list[i]
    discountnum.append(temp)
setnum = min(discountnum) # 有幾個set

# 算在set裡但不組成set的商品數量
left_discountnum = []
for i in range(len(discountnum)):
    left_discountnum.append(discountnum[i]-setnum)   
    
price1 = [] # 20% off
price2 = [] # 10% off
price3 = [] # 原價
for i in product_set_list:
    price1.append(product_price_list[i]*0.8)
    price2.append(product_price_list[i]*0.9)
    price3.append(product_price_list[i])

# 原先的價格
originalprice = 0
for i in range(len(product_price_list)):
    originalprice += product_that_purchased_list[i]*product_price_list[i]

discount_8 = 0 # 能買幾組8折
while setnum - 5 >= 0:
    discount_8 += 1
    setnum -= 5     # 現在setnum帶表能買幾組9折

totalprice = 0
# 把8折9折的set先算出來
for i in range(len(price1)):    
    totalprice += 5 * discount_8 * price1[i]
    totalprice += setnum*price2[i]
# 算set剩下的
for i in range(len(left_discountnum)):
    totalprice += left_discountnum[i] * price3[i]
# 算不在set裡的
out_of_set_price_list = []
out_of_set_purchased_list = []
for i in range(num_of_products):
    if not (i in product_set_list): 
        out_of_set_price_list.append(product_price_list[i])
        out_of_set_purchased_list.append(product_that_purchased_list[i])

for i in range(len(out_of_set_price_list)):
    totalprice += out_of_set_price_list[i] * out_of_set_purchased_list[i]

# 省下的錢
saved_amount = originalprice - totalprice



# 可招的部員
menbers_join_in = saved_amount // 1000

# output
if menbers_join_in >= 1:
    print(int(totalprice), int(menbers_join_in), sep=",")
else:
    print("So sad. I messed up.")