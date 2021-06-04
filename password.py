# 密碼重複測試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入三次
# 如果正確 就印出 "登入成功!"
# 如果不正確 就印出 "密碼錯誤! 還有_次機會!"
password = 'a123456'
i = 3 #剩餘機會

while i > 0:
    i = i - 1
    pwd = input('Please type in the password: ')
    if pwd == password:
        print('Lon in success')
        break #逃出迴圈
    else:
        print('Wrong password')
        #剩餘0次不要印
        if i > 0:
            print('You have', i, 'chances')
        else:
            print('You are locked')

