# abby chang

step_num_and_food_kg_str = input()      # 第一行有兩數n跟x
step_num_and_food_kg = step_num_and_food_kg_str.split(",")     # 把兩數變成一個list   # in list, there are all str.
    # ['n','x']
step_kg_and_step_price_str = input()   # 第二行有2n個正整數
step_kg_and_step_price = step_kg_and_step_price_str.split(",") # 把2n個數變成一個list    # in list, there are all str.
    # ['','','','',.....,'']

previous_step_upperbound = 0    # 儲存前一個級距的上界
expense = 0     #總花費
food = int(step_num_and_food_kg[1])  # 需要的食材公斤數 # X
expense_that_may_be_lower_list = []     # 儲存food以後的各公斤數價錢

# 這裡先算當前要買的食物的價錢
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
    
# food結束
# 開始算food到最後一個級距的價錢    
    
for quantity in range(food, (current_step_upperbound +1)):   # 檢查food以上的數量之價錢是否小於或等於該數量之價錢   # 這樣的話還要跑迴圈 # 跑同一個級距迴圈
    previous_step_upperbound = 0    # 將變數重新指派成原始值
    expense_that_may_be_lower = 0
    
    for i in range(int(step_num_and_food_kg[0])):   # 跑級距數次迴圈
        current_step_upperbound = int(step_kg_and_step_price[i])   # 將清單中第i個數設為當前級距上界
        current_step_price = int(step_kg_and_step_price[i+int(step_num_and_food_kg[0])])   # 將清單中第i+n個數設為當前級距價錢
        
        if (quantity > previous_step_upperbound) and (quantity >= current_step_upperbound):
            amount_to_buy_in_current_step_2 = (current_step_upperbound - previous_step_upperbound)
        elif (quantity > previous_step_upperbound) and (quantity < current_step_upperbound):     # 假設需要的食材公斤數大於下界且小於當前級距上界
            amount_to_buy_in_current_step_2 = quantity - previous_step_upperbound
        else:   # 假設需要的食材公斤數小於或等於下界
            amount_to_buy_in_current_step_2 = 0
        expense_that_may_be_lower += amount_to_buy_in_current_step_2 * current_step_price       
        previous_step_upperbound = current_step_upperbound      # 將當前級距上界儲存成前級距上界
    expense_that_may_be_lower_list.append(expense_that_may_be_lower)

for i in range(len(expense_that_may_be_lower_list)):   # food要儲存成最小的quantity # 給food以後的quantity一個list給他們編號
    if expense_that_may_be_lower_list[i] <= expense:
        expense = expense_that_may_be_lower_list[i]
        i_that_makes_a_better_price = i

food = food + i_that_makes_a_better_price
      
# output
print(food, expense, sep=",")