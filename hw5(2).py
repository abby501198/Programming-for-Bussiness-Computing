# abby chang

import math

line_list = []  # 設一個放圖形的list
while True:  # 將線一條條放進line_list
    current_list = input()
    if current_list == "LINESTOP":  # 若遇到LINESTOP就停止讀取線的資料
        degree = float(input())  # 並讀取旋轉角度
        break
    else:
        line_list.append(current_list.split(","))   # 將線放進line_list裡


def rotate(line_list, degree=90):   # 定義一個讓圖形旋轉的函數
    angle = math.radians(degree)    # 將度數轉為弧度
    new_line_list = []  # 設一個空的list放新的圖形
    for line in line_list:  # 將線個別取出
        new_line = [0, 0, 0, 0]    # 每跑一條新的線就清空list的內容物
        for i in range(len(line)):
            if i % 2 == 0:  # 將x套用x的旋轉公式
                new_line[i] = float(line[i]) * math.cos(angle) + float(line[i+1]) * -math.sin(angle)
            else:   # 將y套用y的旋轉公式
                new_line[i] = float(line[i-1]) * math.sin(angle) + float(line[i]) * math.cos(angle)
        new_line_list.append(new_line)  # 將旋轉後的線放入new_line_list
    return new_line_list    # 回傳旋轉後的圖形

new_line_list = rotate(line_list, degree)   # 使用該函數


def printlines(line_list):  # 此為將答案輸出的函數
    for i, aline in enumerate(line_list):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))

printlines(new_line_list)   # 使用該函數
