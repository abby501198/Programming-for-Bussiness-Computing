# abby chang

num_of_objects_and_limitation_str = input() # 物品個數與負重上限
num_of_objects_and_limitation_list = num_of_objects_and_limitation_str.split(",")
num_of_objects = int(num_of_objects_and_limitation_list[0]) # 物品個數
limitation = int(num_of_objects_and_limitation_list[1]) # 負重上限
weight_of_objects_str = input() # 物品重量
weight_of_objects_list = weight_of_objects_str.split(",")
utility_of_objects_str = input()    # 物品效用
utility_of_objects_list = utility_of_objects_str.split(",")
existence_str = input() # 是否有帶
existence_list = existence_str.split(",")

total_weight = 0
total_utility = 0
# 算出總重量及總效用
for i in range(num_of_objects):
    total_weight += int(weight_of_objects_list[i]) * int(existence_list[i])
    total_utility += int(utility_of_objects_list[i]) * int(existence_list[i])
# 判斷總重量有無超出負重上限
if total_weight <= limitation:
    print(total_weight, total_utility, sep = ",")
else:
    print(-1)


