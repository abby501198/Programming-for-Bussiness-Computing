# abby chang

w0 = 0.5 # 初始意願值
ap = int(input()) # pm2.5濃度
tmp = int(input()) # 氣溫
dp = int(input()) # 露點溫度
cv = float(input()) # 赴約臨界值
rh = 100 - 5 * (tmp - dp) # 相對溼度公式

if ap <= 35:                                  # 空汙影響意願值算式
  w_ap = w0 + (100 - ap) * 0.005
else:
  w_ap = w0 + (45 - ap) * 0.02


if rh <= 30:                                  # 相對濕度影響意願值算式
  w_rh = w0 / 60 * (110 - rh)
else:
  w_rh = w0 / 45 * (90 - rh)

if w_ap <= 0:       # 大於小於0之設定
  w_ap = 0
elif w_ap >= 1:
  w_ap = 1
  
if w_rh <= 0:
  w_rh = 0
elif w_rh >= 1:
  w_rh = 1
  
if w_ap <= w_rh:   # 意願值比大小
  final_w = w_ap
else:
  final_w = w_rh

# output
print('{:.2f}'.format(final_w))

if final_w >= cv:
  print("Let's go together.")
else:
  print("I wouldn't go out with you.")