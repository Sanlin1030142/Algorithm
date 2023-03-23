# 演算法分析機測
# 學號: 10927108 / 10927110 / 10927126
# 姓名: 劉珈彤   / 姜柏仰    / 劉丞曜
# 中原大學資訊工程系


import time

# do
"""
宣告陣列friend_list
用於存放好友列表
宣告陣列is_used
用於判斷是否已經用過

"""
# input
"""
array_size 正整數
用來表示總共有多少人
array_value
用來表示每個人對應的好友
"""
# 輸出
"""
顯示小群體的數量
以換行字元做結尾
"""

# 做遞迴
def SmallGroups(i):
    if is_used[i]== 0:
        is_used[i] = 1
        SmallGroups(int(friend_list[i]))
    return
    
    
# 程式開始
start_time = time.time()

print("Small Groups!")
# 好友人數
friend_size = input()
friend_size = int(friend_size)
# 初始化清單
is_used = [0]*friend_size

# 當好友人數不等於0時
while int(friend_size) != 0  :
    single_friend = input()
    friend_list = single_friend.split(" ")
    # 變成int type
    for x in range(len(friend_list) ):
        friend_list[x] = int(friend_list[x])
    # 呼叫小群體function

    # 從0開跑完所有的friend list
    # 跳過所有已經被處理過的資料
    ans = 0
    
    for x in range(friend_size):
        if is_used[x] == 0:
            ans = ans+1 
            SmallGroups(x)

    # 輸出
    print(ans)
    friend_size = input()


total_time = time.time() - start_time
print(total_time)