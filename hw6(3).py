# abby chang
'''
聯發科,聯電,台積電
零股交易,零股,景氣,景氣好,景氣燈號,預告,法說,意外
盤中零股交易上路、聯發科 聯電法說、9月景氣燈號 本周大事預告
國泰證券10月投資氣象 正向看待美股 聚焦4大產業
台積電南科晶圓18廠傳意外 台積電：不影響生產營運。聯發科聯電：已充分檢查工廠
INPUT_END
'''
companylist = input().split(',')
keywordlist = input().split(',')

newslist = []
while True:
    news = input().replace(' ','')
    if news != 'INPUT_END':
        newslist.append(news)
    else:
        break

keywordlist.sort(key=len, reverse=True)

for title in newslist:
    # company
    currentidx = []
    for company in companylist:
        idx = title.find(company)
        if idx != -1:
            currentidx.append([company, idx])
    currentidx.sort(key= lambda x:(x[1],x[0]))
'''
currentidx = 
[['聯發科', 9], ['聯電', 12]]
[]
[['台積電', 0], ['聯發科', 25], ['聯電', 28]]
'''
    # 找關鍵字斷詞
    keyidxlist = []
    for keyword in keywordlist:
        idx = title.find(keyword)