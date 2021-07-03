# abby chang

current_num = int(input())  # 輸入的四位數 int
final_num_list = []     # 創造一個list放每一個迴圈的結果

while True:    # 無限迴圈
       
    current_num_list = []   # 創造一個空list讓輸入的四位數可變成list
    if current_num < 10:                            # 用三個if補0
        current_num = int(str(current_num) + str(000)) 
    if 10 <= current_num < 100:
        current_num = int(str(current_num) + str(00))
    if 100 <= current_num <1000:
        current_num = int(str(current_num) + str(0))

    for num in str(current_num):    # 把輸入的四位數依序放進list
        current_num_list.append(num)    #in list, there are all int.
   
    current_num_list.sort()     # 將四位數由小到大排序
   
    small_to_big_list = current_num_list    # 把排序好的list重新命名
    
    smallest = int(small_to_big_list[0] + small_to_big_list[1] + small_to_big_list[2] + small_to_big_list[3])   # 由小到大組成最小數
    biggest = int(small_to_big_list[3] + small_to_big_list[2] + small_to_big_list[1] + small_to_big_list[0])    #由大到小組成最大數

    current_num = biggest - smallest    # 最大、最小數相減
    
    final_num_list.append(current_num)      # 把每圈結果放進list裡
    
    if current_num == 6174:     # 若一開始currnt_num就是6174時，直接脫離迴圈並印出6174
        break 
    
# output
print(*final_num_list , sep=",")    # 將所有數字印在同行並以","隔開數字及數字