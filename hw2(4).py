# abby chang

days_sleep = int(input()) 
sleeptime_over_7 = 0
total_sleeptime = 0

for days in range(days_sleep):
    sleeptime = float(input())
    if sleeptime > 7:
        sleeptime_over_7 += 1
    total_sleeptime += sleeptime

average_sleeptime = total_sleeptime / days_sleep


lemonmask = sleeptime_over_7
sleeptime_under_and_equal_to_7 = days_sleep - sleeptime_over_7

if average_sleeptime <= 6:
    honeymask = sleeptime_under_and_equal_to_7
    eggmask = 0
else:
    eggmask = sleeptime_under_and_equal_to_7
    honeymask = 0

lemon = lemonmask * 1.5
oil = (lemonmask * 4) + (honeymask * 9)
honey = (honeymask * 18) + (eggmask * 6)
egg = eggmask * 2

if lemon % 1 != 0:
    lemon = (lemon // 1) +1

if egg % 3 != 0:
    egg_box = (egg//3) + 1
else:
    egg_box = egg // 3
    
if lemon >= 5:
    lemon = lemon * 0.9
    
money = (lemon * 7) + (oil *0.6) + (honey * 1.2) + (egg_box * 25)
money = int(money)

print(money)