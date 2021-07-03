# abby chang

records = []    # 設一個二維list放打擊紀錄表格
while True:  # 將紀錄一筆一筆放進表格
    current_record = input()
    if current_record == "RECORDSTOP":  # 若遇到RECORDSTOP則停止讀取資料
        break   # 並跳出迴圈
    else:
        records.append(current_record.split(","))   # 將記錄放進表格

functions = []  # 設一個二維list放需進行的項目
while True:
    current_function = input()
    if current_function == "FUNCTIONSTOP":  # 若遇到FUNCTIONSTOP則停止讀取資料
        break   # 並挑出迴圈
    else:
        functions.append(current_function.split(" "))   # 將須讀取的資料放進此list


def player_avg(seasons, records, player_number):    # 定義計算指定球員在指定球季的打擊率的函數
    atbats = 0  # 打數
    hits = 0    # 安打數
    for current_record in records:  # 讀取表格中各列資料
        if (int(current_record[1]) == player_number) and (current_record[2] in seasons):    # 當前資料與指定球員及指定球季相符
            atbats += int(current_record[3])    # 累加各季的打數
            hits += int(current_record[4])  # 累加各季的安打數
    batting_average = hits / atbats     # 計算該球員的打擊率
    print(chop(batting_average))    # 將打擊率取到小數點後第二位並將其印出
    return chop(batting_average)    # 回傳該數值


def team_avg(seasons, records, team_name):  # 定義計算指定球隊在指定球季的打擊率的函數
    atbats = 0  # 打數
    hits = 0    # 安打數
    for current_record in records:  # 讀取表格中各列資料
        if (current_record[0] == team_name) and (current_record[2] in seasons):    # 當前資料與指定球隊及指定球季相符
            atbats += int(current_record[3])    # 累加各季的打數
            hits += int(current_record[4])  # 累加各季的安打數
    batting_average = hits / atbats     # 計算該球隊的打擊率
    return chop(batting_average)    # 將打擊率取到小數點後第二位並回傳該數值


def best_player(seasons, records):  # 定義計算指定球季的最佳球員的函數
    best_player_list = []   # 放最佳球員的list
    for i in range(len(seasons)):   # 當前球季
        highest_batting_average = -1    # 最高打擊率
        for current_record in records:  # 讀取表格中各列資料
            if current_record[2] == seasons[i]:    # 當前資料與指定球季相符
                current_batting_average = int(current_record[4]) / int(current_record[3])   # 計算當前打擊率
                if current_batting_average > highest_batting_average:   # 若當前打擊率高於最佳打擊率
                    highest_batting_average = current_batting_average   # 則取代最佳打擊率
                    best_player = int(current_record[1])    # 並成為最佳球員
                    best_atbats = int(current_record[3])    # 及最佳打數
                elif current_batting_average == highest_batting_average:    # 若打擊率相同
                    if int(current_record[3]) < best_atbats:    # 則比打數，打數小者
                        best_player = int(current_record[1])    # 成為最佳球員
                        best_atbats = int(current_record[3])    # 及最佳打數
                    elif int(current_record[3]) == best_atbats:  # 若打數相等
                        if int(current_record[1]) < best_player:    # 則比編號，編號較小者
                            best_player = int(current_record[1])    # 成為最佳球員
        best_player_list.append(best_player)    # 將最佳球員放進list
    print(*best_player_list, sep=",")    # 並print出該list
    return best_player_list  # 回傳該list


def best_team(seasons, records):    # 定義計算指定球季的最佳球隊的函數
    best_team_list = []  # 放最佳球隊的list
    for i in range(len(seasons)):   # 當前球季
        highest_batting_average = -1    # 最高打擊率
        best_team = 0   # 最佳球隊
        team_counted_list = []  # 放計算過的隊伍的list
        for current_record in records:  # 讀取表格中各列資料
            if (current_record[2] == seasons[i]) and (current_record[0] not in team_counted_list):  # 若資料符合指定球季且該球隊未算過
                team_counted_list.append(current_record[0])  # 將該球隊放進list以標示為被計算過
                current_batting_average = team_avg(seasons[i], records, current_record[0])  # 計算該球隊當季的打擊率
                if current_batting_average > highest_batting_average:   # 若當前打擊率高於最佳打擊率
                    highest_batting_average = current_batting_average   # 則取代最佳打擊率
                    best_team = current_record[0]    # 並成為最佳球隊
                    best_atbats = int(current_record[3])    # 及最佳打數
                elif current_batting_average == highest_batting_average:    # 若打擊率相同
                    if int(current_record[3]) < best_atbats:    # 則比打數，打數小者
                        best_team = current_record[0]    # 成為最佳球隊
                        best_atbats = int(current_record[3])    # 及最佳打數
                    elif int(current_record[3]) == best_atbats:  # 若打數相等
                        if current_record[0] < best_team:    # 則比編號，編號較小者
                            best_team = current_record[0]     # 成為最佳球隊
        best_team_list.append(best_team)    # 將最佳球隊放進list
    print(*best_team_list, sep=",")    # 並print出該list
    return best_team_list   # 回傳該list


def chop(avg):  # 無條件捨去到小數點第二為時的函數
    avg = int(avg * 100) / 100
    return avg if avg > 0 else 0


for current_function in functions:
    seasons = current_function[1].split(",")
    if int(current_function[0]) == 1:   # 計算球員打擊率
        player_number = int(current_function[2])
        player_avg(seasons, records, player_number)
    if int(current_function[0]) == 2:   # 計算球隊打擊率
        team_name = current_function[2]
        print(team_avg(seasons, records, team_name))  # 找出表現最佳球員
    if int(current_function[0]) == 3:
        best_player(seasons, records)
    if int(current_function[0]) == 4:   # 找出表現最佳球隊
        best_team(seasons, records)
