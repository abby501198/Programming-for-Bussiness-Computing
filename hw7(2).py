# abbby chang

# input
items = input()
genres = input()
targetid = input()

# 讀取u.item
openditems = open(items, 'r', encoding='ISO-8859-1')
# 並將item去除換行後，以"|"切割後，加入itemlist
itemlist = []
for item in openditems:
    itemstripped = item.strip('\n')
    itemsplit = itemstripped.split('|')
    itemsplit.remove(itemsplit[3])  # 去除網址前的空白
    itemlist.append(itemsplit)
openditems.close()
# 關閉檔案

# 讀取u.genre
opendgenres = open(genres, 'r', encoding='ISO-8859-1')
# 並將genre以"|"切割後，將分類名稱加入itemlist
genrelist = []
for genre in opendgenres:
    genresplit = genre.split('|')
    genrelist.append(genresplit[0])
opendgenres.close()
genrelist.remove(genrelist[-1])

# 先看找不找得到對應的movie
for item in itemlist:
    if targetid == item[0]:
        targetitem = item
        break
    else:
        targetitem = 0

# 建一個dictionary放genre(index為key,類別名稱為value)
genredict = {}
for i in range(4, 23):
    genredict[i] = genrelist[i-4]

# output
if targetitem == 0:
    print("No movie found.")    # 找不到就print"No movie found."
else:
    ans = []    # 找得到就將該電影與genre對照，找出所屬genre
    for i in range(4, 23):
        if targetitem[i] == '1':
            ans.append(genredict[i])
    print(targetitem[1] + ':', end=' ')
    print(*ans, sep=', ')
