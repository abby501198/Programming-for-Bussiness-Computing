# abby chang

# input
strings_list = []
while True:
    string = input().strip(" ")  # 去除多餘的空白
    if string == "INPUT_END":   # 若遇到INPUT_END則停止讀取資料
        break   # 並跳出迴圈
    else:
        strings_list.append(string)  # 將各行字串加入string_list

key_string = strings_list[0]    # 把關鍵字取出來

strings_list.remove(key_string)  # 移除關鍵字

new_strings = " ".join(strings_list)  # 將其餘的字串以單一空白串接

index_match = []    # 設一個list放關鍵字對應的index
previous_index = new_strings.find(key_string)   # 將找到的index放進list
if previous_index != -1:  # 若有找到關鍵字
    index_match.append(previous_index)   # 將index放入該list

while previous_index != -1:  # 當還有關鍵字時
    # 從上個index後一個字繼續查找關鍵字
    current_index = new_strings.find(key_string, previous_index+1)
    previous_index = current_index   # 此index成為前一個index
    if current_index != -1:  # 當找到關鍵字時
        index_match.append(current_index)   # 放入該list

if len(index_match) != 0:  # 若有找到與關鍵字相符的字串
    for i in index_match:   # 將關鍵字的index一一取出
        if i >= 7:  # 若關鍵字前面大於七字
            current_string = new_strings[i-7:i] + "**" + key_string + "**" + new_strings[i+len(key_string):i+len(key_string)+7]
        else:   # 若關鍵字前面小於七字
            current_string = new_strings[:i] + "**" + key_string + "**" + new_strings[i+len(key_string):i+len(key_string)+7]
        print(current_string)
else:   # 若無找到與關鍵字相符的字串
    print("NO_MATCH")
