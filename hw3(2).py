# abby chang

step_num_and_food_kg_str = input()      # 第一行有兩數n跟x
step_num_and_food_kg = step_num_and_food_kg_str.split(",")     # 把兩數變成一個list   # in list, there are all str.

step_kg_and_step_price_str = input()   # 第二行有2n個正整數
step_kg_and_step_price = step_kg_and_step_price_str.split(",") # 把2n個數變成一個list    # in list, there are all str.

previous_step_upperbound = 0    # 儲存前一個級距的上界
expense = 0     #總花費
food = int(step_num_and_food_kg[1])  # 需要的食材公斤數

for i in range(int(step_num_and_food_kg[0])):   # 跑級距數次迴圈
    current_step_upperbound = int(step_kg_and_step_price[i])   # 將清單中第i個數設為當前級距上界
    current_step_price = int(step_kg_and_step_price[i+int(step_num_and_food_kg[0])])   # 將清單中第i+n個數設為當前級距價錢
    
    if (food > previous_step_upperbound) and (food >= current_step_upperbound):     # 假設需要的食材公斤數大於下界且大於或等於當前級距上界 
        amount_to_buy_in_current_step = (current_step_upperbound - previous_step_upperbound)
    elif (food > previous_step_upperbound) and (food < current_step_upperbound):     # 假設需要的食材公斤數大於下界且小於當前級距上界
        amount_to_buy_in_current_step = food - previous_step_upperbound
    else:   # 假設需要的食材公斤數小於或等於下界
        amount_to_buy_in_current_step = 0
    expense += amount_to_buy_in_current_step * current_step_price   # 總花費
    previous_step_upperbound = current_step_upperbound      # 將當前級距上界儲存成前級距上界
# output
print(expense)