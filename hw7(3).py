# abby chang

# input
news_title = input()
news_dict = input()
company_category = input()
targetcategory_quantity_round = input().split(',')

# 開啟新聞標題檔案，將每行去除空白及換行後做成list
opendnews_title = open(news_title, 'r', encoding='utf-8')
news_title_list = []
for aline in opendnews_title:
    aline = aline.replace(' ', '')
    aline = aline.strip('\n')
    news_title_list.append(aline)
opendnews_title.close()

# 開啟關鍵字詞點檔案，將每行去除換行並以空白切割成list後，做成dictionary
opendnews_dict = open(news_dict, 'r', encoding='utf-8')
news_dict = dict()
keywordlist = []
for item in opendnews_dict:
    item = item.strip('\n')
    item = item.split(' ')
    keywordlist.append(item[0])  # 並做一個關鍵字集合
    news_dict[item[0]] = int(item[1])
opendnews_dict.close()

# 開啟公司類別檔案，將每行去除換行並以空白切割成list後，做成dictionary
opendcompany_category = open(company_category, 'r', encoding='utf-8')
company_category_dict = dict()
companylist = []
for item in opendcompany_category:
    item = item.strip('\n')
    item = item.split(' ')
    companylist.append(item[0])  # 做一個公司集合
    if item[1] not in company_category_dict:
        company_category_dict[item[1]] = [item[0]]
    else:
        company_category_dict[item[1]].append(item[0])

# 處理第四個input
targetcategory = targetcategory_quantity_round[0]   # 目標產業
totalquantity = int(targetcategory_quantity_round[1])   # 目標購買數量
roundpurchased_list = targetcategory_quantity_round[2].split(':')   # 每輪購買數量

# hw6(3)開始
keywordlist.sort(key=len, reverse=True)  # 將關鍵字照長度排序

if targetcategory not in company_category_dict:  # 若找不到目標產業
    print('NO_MATCH')
else:   # 若找得到目標產業
    targetcategory_grades_dict = dict()
    for company in company_category_dict[targetcategory]:   # 做一個dictionary放該產業所有公司的分數
        targetcategory_grades_dict[company] = 0

    for title in news_title_list:   # 跑每行新聞
        # 若有目標產業之公司出現在新聞中
        for categorycompany in company_category_dict[targetcategory]:
            appear = title.find(categorycompany)
            if appear == -1:    # 找不到
                continue
            else:   # 找到了就開始斷詞
                targetcompany = categorycompany     # 此公司為目標公司

            keyword_index_list = []     # 放關鍵字index的list
            for key in keywordlist:     # 找關鍵字
                idx = title.find(key)
                title_tmp = title   # 暫存該新聞
                while idx != -1:
                    keyword_index_list.append([idx, len(key)])
                    title_tmp = title_tmp.replace(key, ' '*len(key), 1)  # 挖空找到的關鍵字
                    idx = title_tmp.find(key)
            keyword_index_list.sort()   # 排序關鍵字的index

            keyword_index_list_new = []     # 去除重疊的關鍵字
            for i in range(len(keyword_index_list)):
                if i == 0:
                    keyword_index_list_new.append(keyword_index_list[i])
                else:
                    last = keyword_index_list_new[-1]

                    index0 = last[0]
                    len0 = last[1]

                    index1 = keyword_index_list[i][0]
                    len1 = keyword_index_list[i][1]

                    if index0 + len0 > index1 and len0 < len1:
                        keyword_index_list_new[-1] = keyword_index_list[i]

                    elif index0 + len0 > index1 and len0 >= len1:
                        continue
                    else:
                        keyword_index_list_new.append(keyword_index_list[i])
            # 將找到的關鍵字對照權重並計分
            for i in range(len(keyword_index_list_new)):
                keyidx = keyword_index_list_new[i][0]
                keylen = keyword_index_list_new[i][1]
                keyword = title[keyidx:keyidx+keylen]
                targetcategory_grades_dict[targetcompany] += news_dict[keyword]
    # 將分數由高至低排序
    targetcategory_grades_sorted = sorted(targetcategory_grades_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)

    # 開始分配每公司購買的張數
    ans = []
    currentpurchased = 0
    # 若該產業公司數量大於購買公司數
    if len(targetcategory_grades_sorted) >= len(roundpurchased_list):
        for i in range(len(roundpurchased_list)):
            ans.append(0)
        while currentpurchased < totalquantity:
            for i in range(len(ans)):
                if currentpurchased + int(roundpurchased_list[i]) <= totalquantity:
                    ans[i] += int(roundpurchased_list[i])
                    currentpurchased += int(roundpurchased_list[i])
                else:
                    if currentpurchased < totalquantity:
                        ans[i] += (totalquantity - currentpurchased)
                        currentpurchased += int(roundpurchased_list[i])
                    else:
                        break
    # 若該產業公司數量小於購買公司數
    else:
        for i in range(len(targetcategory_grades_sorted)):
            ans.append(0)
        while currentpurchased < totalquantity:
            for i in range(len(ans)):
                if currentpurchased + int(roundpurchased_list[i]) <= totalquantity:
                    ans[i] += int(roundpurchased_list[i])
                    currentpurchased += int(roundpurchased_list[i])
                else:
                    if currentpurchased < totalquantity:
                        ans[i] += (totalquantity - currentpurchased)
                        currentpurchased += int(roundpurchased_list[i])
                    else:
                        break

    # output
    # 不為0張才輸出
    for i in range(len(ans)):
        if ans[i] != 0:
            print(targetcategory_grades_sorted[i][0] + '購買' + str(ans[i]) + '張')
