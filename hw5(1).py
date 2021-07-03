# abby chang

line_list = []  # 設一個放圖形的list
while True:  # 將線一條條放進line_list
    current_list = input()
    if current_list == "LINESTOP":  # 若遇到LINESTOP就停止讀取線的資料
        shift_list = input().split(",")  # 並讀取平移量
        break
    else:
        line_list.append(current_list.split(","))   # 將線放進line_list裡

xshift = float(shift_list[0])   # x的平移量
yshift = float(shift_list[1])   # y的平移量


def plotshift(line_list, xshift=0, yshift=0):   # 定義一個讓圖形位移的函數
    for line in line_list:  # 將線個別取出
        for i in range(len(line)):
            if i % 2 == 0:  # 將x項加x的平移量
                line[i] = float(line[i]) + xshift
            else:           # 將y項加y的平移量
                line[i] = float(line[i]) + yshift
    return line_list    # 回傳平移後的圖形

plotshift(line_list, xshift, yshift)    # 使用該函數


def printlines(line_list):  # 此為移將答案輸出的函數
    for i, aline in enumerate(line_list):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))

printlines(line_list)   # 使用該函數
