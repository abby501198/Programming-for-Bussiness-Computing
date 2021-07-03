# abby chang

# input
strings_list = []
while True:
    string = input().strip(" ")  # 去除多餘的空白
    if string == "INPUT_END":   # 若遇到INPUT_END則停止讀取資料
        break   # 並跳出迴圈
    else:
        strings_list.append(string)  # 將各行字串加入string_list

distance = int(strings_list[0])
key_string_1 = strings_list[1]    # 把關鍵字取出來
key_string_2 = strings_list[2]

strings_list.remove(strings_list[0])
strings_list.remove(key_string_1)  # 移除關鍵字
strings_list.remove(key_string_2)
new_strings = " ".join(strings_list)  # 將其餘的字串以單一空白串接

# correct

def find_key_string(key_string, original_string):
    index_match = []    # 設一個list放關鍵字對應的index
    previous_index = original_string.find(key_string)   # 將找到的index放進list
    if previous_index != -1:  # 若有找到關鍵字
        index_match.append(previous_index)   # 將index放入該list

    while previous_index != -1:  # 當還有關鍵字時
        # 從上個index後一個字繼續查找關鍵字
        current_index = original_string.find(key_string, previous_index+1)
        previous_index = current_index   # 此index成為前一個index
        if current_index != -1:  # 當找到關鍵字時
            index_match.append(current_index)   # 放入該list
    return index_match

index_match_1 = find_key_string(key_string_1, new_strings)
index_match_2 = find_key_string(key_string_2, new_strings)

string_sliced = []  # 設一個放裁切好的字串的list
for key1 in index_match_1:
    for key2 in index_match_2:
        if (key1 < key2) and (key2-(key1+len(key_string_1))) <= distance:
            if key1 >= 7:
                string_sliced.append(new_strings[key1-7:key1] + "**" + key_string_1 + "**" + new_strings[key1+len(key_string_1):key2] + "**" + key_string_2 + "**"+ new_strings[key2+len(key_string_2):key2+len(key_string_2)+7])
            else:
                string_sliced.append(new_strings[:key1] + "**" + key_string_1 + "**" + new_strings[key1+len(key_string_1):key2] + "**" + key_string_2 + "**"+ new_strings[key2+len(key_string_2):key2+len(key_string_2)+7])

if  len(string_sliced) != 0 : # 若有找到與關鍵字相符的字串
    for output_string in string_sliced:
        print(output_string)
else:   # 若無找到與關鍵字相符的字串
    print("NO_MATCH")      
