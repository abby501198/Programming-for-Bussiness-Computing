# abby chang

num_of_objects_and_limitation_str = input() # 物品個數與負重上限
num_of_objects_and_limitation_list = num_of_objects_and_limitation_str.split(",")
num_of_objects = int(num_of_objects_and_limitation_list[0]) # 物品個數
limitation = int(num_of_objects_and_limitation_list[1]) # 負重上限
weight_of_objects_str = input() # 物品重量
weight_of_objects_list = weight_of_objects_str.split(",")
utility_of_objects_str = input()    # 物品效用
utility_of_objects_list = utility_of_objects_str.split(",")

# 第二題演算法
# 算cp值
cp_list = []
for i in range(num_of_objects):
    cp_list.append(int(utility_of_objects_list[i]) / int(weight_of_objects_list[i]))

total_weight_A = 0
total_utility_A = 0
object_can_put_in_bag_A = []

for i in range(num_of_objects):
    biggest_cp_for_now = 0
    # 比CP 比重量 比編號
    for i in range(num_of_objects): # 取出當前的最大CP值
        if cp_list[i] > biggest_cp_for_now: # 比CP值
            biggest_cp_for_now = cp_list[i]
            object_now_A = i  # 儲存當前的index
            biggest_cp_for_now_weight = int(weight_of_objects_list[i])
        elif cp_list[i] == biggest_cp_for_now:   # 比重量
            if int(weight_of_objects_list[i]) < biggest_cp_for_now_weight:
                object_now_A = i
            elif int(weight_of_objects_list[i]) == biggest_cp_for_now_weight:    # 比編號
                if i < object_now_A:
                    object_now_A = i
 
    total_weight_A += int(weight_of_objects_list[object_now_A]) # 總重先加當前物品重量
    if total_weight_A <= limitation:  # 若總重小於負重上限則放進背包
        object_can_put_in_bag_A.append(object_now_A)
    else:   # 若總重超出負重上限則將總重扣除當前物品重量
        total_weight_A -= int(weight_of_objects_list[object_now_A])
    cp_list[object_now_A] = 0 # 將算過的CP值設定成0

for i in object_can_put_in_bag_A: # 算出演算法一的總效用
    total_utility_A += int(utility_of_objects_list[i])
    

# 將放進背包的index加一並排序
for i in range(len(object_can_put_in_bag_A)): 
    object_can_put_in_bag_A[i] = object_can_put_in_bag_A[i] + 1
object_can_put_in_bag_A.sort()

# 本題演算法
total_weight_B = 0
total_utility_B = 0
object_can_put_in_bag_B = []

for i in range(num_of_objects):
    biggest_utility_for_now = 0
    # 比效用 比重量 比編號
    for i in range(num_of_objects):
        if int(utility_of_objects_list[i]) > biggest_utility_for_now:   # 比效用
            biggest_utility_for_now = int(utility_of_objects_list[i])
            object_now_B = i
            biggest_utility_for_now_weight = weight_of_objects_list[i]
        elif int(utility_of_objects_list[i]) == biggest_utility_for_now:    # 比重量
            if weight_of_objects_list[i] < biggest_utility_for_now_weight:
                object_now_B = i
            elif weight_of_objects_list[i] == biggest_utility_for_now_weight:   # 比編號
                if i < object_now_B:
                    object_now_B = i
             
    total_weight_B += int(weight_of_objects_list[object_now_B]) # 總重先加當前物品重量
    if total_weight_B <= limitation:    # 若總重小於負重上限則放進背包
        object_can_put_in_bag_B.append(object_now_B)
        total_utility_B  += int(utility_of_objects_list[object_now_B])  # 若可放進背包，總效用加當前商品效用
    else:   # 若總重超出負重上限則將總重扣除當前物品重量
        total_weight_B -= int(weight_of_objects_list[object_now_B])
    utility_of_objects_list[object_now_B] = 0   # 將算過的效用設定成0

# 將放進背包的index加一並排序    
for i in range(len(object_can_put_in_bag_B)):
    object_can_put_in_bag_B[i] = object_can_put_in_bag_B[i] + 1
object_can_put_in_bag_B.sort()

#output
if total_utility_A >= total_utility_B : # 若演算法一總效用大於等於演算法二總效用
    print(*object_can_put_in_bag_A, sep = ",")  # 則選用演算法一結果
else:   # 若演算法二總效用較大
    print(*object_can_put_in_bag_B, sep = ",")  # 則選用演算法二結果