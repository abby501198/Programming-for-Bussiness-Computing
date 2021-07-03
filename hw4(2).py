# abby chang

num_of_objects_and_limitation_str = input() # 物品個數與負重上限
num_of_objects_and_limitation_list = num_of_objects_and_limitation_str.split(",")
num_of_objects = int(num_of_objects_and_limitation_list[0]) # 物品個數
limitation = int(num_of_objects_and_limitation_list[1]) # 負重上限
weight_of_objects_str = input() # 物品重量
weight_of_objects_list = weight_of_objects_str.split(",")
utility_of_objects_str = input()    # 物品效用
utility_of_objects_list = utility_of_objects_str.split(",")

# 算cp值
cp_list = []
for i in range(num_of_objects):
    cp_list.append(int(utility_of_objects_list[i]) / int(weight_of_objects_list[i]))

total_weight = 0
object_can_put_in_bag = []

for i in range(num_of_objects):
    biggest_cp_for_now = 0
    for i in range(num_of_objects): # 取出當前的最大CP值
        if cp_list[i] >= biggest_cp_for_now:
            biggest_cp_for_now = cp_list[i]
            object_now = i  # 儲存當前的index
   
    total_weight += int(weight_of_objects_list[object_now]) # 總重先加當前物品重量
    if total_weight <= limitation:  # 若總重小於負重上限則放進背包
        object_can_put_in_bag.append(object_now)
    else:   # 若總重超出負重上限則將總重扣除當前物品重量
        total_weight -= int(weight_of_objects_list[object_now])
    cp_list[object_now] = 0 # 將算過的CP值設定成0

# 將放進背包的index加一並排序
for i in range(len(object_can_put_in_bag)): 
    object_can_put_in_bag[i] = object_can_put_in_bag[i] + 1
object_can_put_in_bag.sort()

#output
print(*object_can_put_in_bag, sep = ",")
