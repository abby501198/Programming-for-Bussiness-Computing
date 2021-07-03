# abby chang

current_num = int(input()) # 輸入的三位數
loopCounter = 0    # loopCounter

while loopCounter <= 2:  # 重複三次
    maxi = 0           # 最大值
    mini = 9           # 最小值
    mid = 0            # 中間值
   
    if current_num < 10:         # 補0
        current_num = int(str(current_num) + str(00)) 
    if 10 <= current_num < 100:
        current_num = int(str(current_num) + str(0))
   
    for i in str(current_num):   # 把輸入的三位數分開比大小
        if int(i) >= maxi:    
               maxi = int(i)

        if int(i) <= mini:
               mini = int(i)
 
        if mini <= int(i) <= maxi:
               mid = int(i)
  
    biggest = int(str(maxi) + str(mid) + str(mini))  # 三位數的最大組合
    smallest = int(str(mini) + str(mid) + str(maxi)) # 三位數的最小組合
    current_num = biggest - smallest # 結果
 
    if loopCounter == 0:
        num1 = current_num 
    if loopCounter == 1:
        num2 = current_num
    else:
        num3 = current_num 

    loopCounter += 1
 
 # output
print(num1,num2,num3,sep = ",")