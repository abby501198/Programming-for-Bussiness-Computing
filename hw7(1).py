# abby chang

import operator

# input
data = input()
keyword = input()

# 讀檔
openddata = open(data, 'r', encoding='utf-8')

# 將每行先拆成兩句，再去除空白跟換行，接著放入list
datalist = []
for aline in openddata:
    newaline = aline.split('\t')
    for i in range(2):
        newaline[i] = newaline[i].strip(' ')
        newaline[i] = newaline[i].strip('\n')
        datalist.append(newaline[i])
openddata.close()
# 關閉檔案


# 找熱門前一個字跟熱門下一個字
# 並數分別有出現幾次
formerdict = dict()
latterdict = dict()
for aline in datalist:
    previouslocation = 0
    while previouslocation != -1:   # 若熱門字出現一次以上
        location = aline.find(keyword, previouslocation)    # 繼續找
        if location == -1:  # 若找不到就break
            break
        if location - 1 >= 0:   # 若熱門前一字有字
            if aline[location - 1] not in formerdict:    # 若該字還不在dictionary中
                formerdict[aline[location - 1]] = 1  # 則新增該字
            else:
                formerdict[aline[location - 1]] += 1  # 否則該字出現次數加一
        if location + len(keyword) <= len(aline) - 1:  # 若熱門後一字有字
            if aline[location + len(keyword)] not in latterdict:    # 若該字還不在dictionary中
                latterdict[aline[location + len(keyword)]] = 1  # 則新增該字
            else:
                latterdict[aline[location + len(keyword)]] += 1  # 否則該字出現次數加一
        previouslocation = location + 1   # 更新previouslocation

# 將此dictionary先依照頻率再依照字的內碼排序
sorted_former = sorted(formerdict.items(), key=operator.itemgetter(1, 0), reverse=True)
sorted_latter = sorted(latterdict.items(), key=operator.itemgetter(1, 0), reverse=True)

# 將排序後前10個字放入答案list
formerans = []
latterans = []
if len(sorted_former) < 10:   # 若不足10個
    for i in range(len(sorted_former)):
        formerans.append(sorted_former[i][0])   # 則全部輸出
else:   # 若足10個
    for i in range(10):
        formerans.append(sorted_former[i][0])   # 則輸出10個
if len(sorted_latter) < 10:  # 若不足10個
    for i in range(len(sorted_latter)):
        latterans.append(sorted_latter[i][0])   # 則全部輸出
else:   # 若足10個
    for i in range(10):
        latterans.append(sorted_latter[i][0])   # 則輸出10個

# output
print('熱門前一個字:')
for ans in formerans:
    print(ans + '---' + keyword)

print('熱門下一個字:')
for ans in latterans:
    print(keyword + '---' + ans)
