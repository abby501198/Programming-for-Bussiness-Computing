# abby chang

num = int(input())  # 共有幾個級距
kg = int(input())   # 公斤數
previousR = 0
total = 0

for i in range(num):  
    r = int(input())
    p = int(input())
    if kg < r: 
        total += (kg - previousR) * p  
        break  
    else:
        r_g = r - previousR  
        total += r_g * p  
        previousR = r  
print(total)