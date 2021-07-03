#  abby chang

num_of_targets_and_budget_and_risk_str = input()    # 投資標的個數、預算，和風險係數
num_of_targets_and_budget_and_risk_list = num_of_targets_and_budget_and_risk_str.split(
    ",")
num_of_targets = int(num_of_targets_and_budget_and_risk_list[0])    # 投資標的個數
budget = int(num_of_targets_and_budget_and_risk_list[1])    # 預算
risk = int(num_of_targets_and_budget_and_risk_list[2])  # 風險係數
price_of_targets_str = input()  # 投資標的價錢
price_of_targets_list = price_of_targets_str.split(",")
expected_return_on_targets_str = input()    # 投資標的的預期報酬
expected_return_on_targets_list = expected_return_on_targets_str.split(",")

# 將價錢及預期報酬轉成整數
for i in range(len(price_of_targets_list)):
    price_of_targets_list[i] = int(price_of_targets_list[i])
for i in range(len(expected_return_on_targets_list)):
    expected_return_on_targets_list[i] = int(
        expected_return_on_targets_list[i])

# 用for把n列input組成矩陣
matrix = []
for i in range(num_of_targets):
    row_str = input()
    row_list = row_str.split(",")
    for i in range(len(row_list)):
        row_list[i] = int(row_list[i])
    matrix.append(row_list)

target_can_put_in_set = []  # 最後要投資的標的
biggest_now = 0  # 目前目標式最大的值
total_cost = 0  # 總花費


while True:
    target_A = -1   # 暫存讓目標式為最大值的投資標的編號
    # 第一輪算法
    for i in range(num_of_targets):
        # 目前投資標的目標式值
        result = expected_return_on_targets_list[i] - (risk * matrix[i][i])
        if result > biggest_now:   # 比投資標的目標式值
            biggest_now = result
            biggest_now_price = price_of_targets_list[i]
            target_A = i
        elif result == biggest_now:
            if price_of_targets_list[i] < biggest_now_price:    # 比價錢
                target_A = i
            elif price_of_targets_list[i] == biggest_now_price:
                if i < target_A:    # 比編號
                    target_A = i
    if target_A != -1:
        total_cost += price_of_targets_list[target_A]
        if total_cost <= budget:  # 若該投資標的沒有超出預算
            target_can_put_in_set.append(target_A)  # 則投資該標的
        else:   # 若超出預算
            total_cost -= price_of_targets_list[target_A]   # 則還原total_cost
    if target_A == -1:  # 若第一輪沒有取到投資標的
        print(0)    # 則print"0"，並結束
        break
    # 第二種算法
    elif target_A != -1:    # 暫存讓目標式為最大值的投資標的編號
        previous_target = target_A  # 前一個投資標的
        target_B = -1   # 當前投資標的
        biggest_now = 0
        # 將算過的預期報酬歸零，使之無法成為最大目標式值
        expected_return_on_targets_list[target_A] = 0
        for i in range(num_of_targets):
            result = expected_return_on_targets_list[i] - (
                risk * (matrix[i][i] + 2 * (matrix[previous_target][i])))    # 目前投資標的目標式值
            if result > biggest_now:    # 比投資標的目標式值
                biggest_now = result
                biggest_now_price = price_of_targets_list[i]
                target_B = i
            elif result == biggest_now:
                if price_of_targets_list[i] < biggest_now_price:    # 比價錢
                    target_B = i
                elif price_of_targets_list[i] == biggest_now_price:
                    if i < target_B:    # 比編號
                        target_B = i
        if target_B != -1:
            total_cost += price_of_targets_list[target_B]
            if total_cost <= budget:    # 若該投資標的沒有超出預算
                target_can_put_in_set.append(target_B)  # 則投資該標的
                previous_target = target_B
            else:   # 若超出預算
                total_cost -= price_of_targets_list[target_B]   # 則還原total_cost
        # 將算過的預期報酬歸零，使之無法成為最大目標式值
        expected_return_on_targets_list[previous_target] = 0
        break   # 每個投資標的都算過後break

for i in range(len(target_can_put_in_set)):  # 將投資標的編號加一並排序
    target_can_put_in_set[i] += 1
target_can_put_in_set.sort()

if len(target_can_put_in_set) != 0:  # 若有投資
    print(*target_can_put_in_set, sep=",")  # 則print出投資標的編號
