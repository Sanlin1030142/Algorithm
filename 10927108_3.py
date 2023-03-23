import operator

__metaclass__ = type

temp = input()
temp = temp.split(" ")

N = int(temp[0])  # 狼
M = int(temp[1])  # 羊
# N = int(input("請輸入狼的數量："))  # 狼
# M = int(input("請輸入羊的數量："))  # 羊
K = 2  # 船的乘坐人數

child = []
open_list = []
closed_list = []


class State:
    def __init__(self, m, n, b):
        self.m = m  # 左岸狼的數量
        self.n = n  # 左岸羊的數量
        self.b = b  # b=1時船在左岸(W)，b=0時船在右岸(E)
        self.g = 0
        self.f = 0  # f=g+h
        self.father = None
        self.node = [m, n, b]


init = State(M, N, 1)
goal = State(0, 0, 0)


def safe(s):
    if s.m > M or s.m < 0 or s.n > N or s.n < 0 or (s.m != 0 and s.m < s.n) or (s.m != M and M - s.m < N - s.n):
        return False
    else:
        return True

# 啟發函數


def h(s):
    return s.m + s.n - K * s.b
    # return M - s.m + N - s.n


def equal(a, b):
    if a.node == b.node:
        return 1, b
    else:
        return 0, b

# 判斷當前狀態與父狀態是否一致


def back(new, s):
    if s.father is None:
        return False
    # 判斷當前狀態與祖父狀態是否一致
    n = b = s.father
    while (1):
        a, n = equal(new, b)
        if a:
            return True
        b = n.father
        if b is None:
            return False


# 將open_list以f值進行排序
def open_sort(l):
    the_key = operator.attrgetter('f')  # 指定屬性排序的key
    l.sort(key=the_key)


# 擴展節點時在open表和closed表中找原來是否存在相同mnb屬性的節點
def in_list(new, l):
    for item in l:
        if new.node == item.node:
            return True, item
    return False, None


def A_star(s):
    A = []
    global open_list, closed_list
    open_list = [s]
    closed_list = []
    # print(len(open_list))
    # print('closed list:')  #選擇印出open表或closed表的變化過程
    # print(s.node)
    # a=1
    while (1):  # open表非空
        # get = open_list[0]  #取出open表第一個元素get
        for i in open_list:
            if i.node == goal.node:  # 判斷是否為目標節點
                A.append(i)
                open_list.remove(i)
        if not (open_list):
            break
        get = open_list[0]
        open_list.remove(get)  # 將get從open表移出
        closed_list.append(get)  # 將get加入closed表

        # 以下得到一個get的新子節點new並考慮是否放入openlist
        for i in range(M+1):  # 上船的狼
            for j in range(N+1):  # 上船的羊
                # 船上非法情況
                if i + j == 0 or i + j > K or (i != 0 and i < j):
                    continue
                # a=a+1
                if get.b == 1:  # 當前船在左岸，下一狀態統計船在右岸的情況
                    new = State(get.m - i, get.n - j, 0)
                    child.append(new)
                    # print(1)
                else:  # 當前船在右岸，下一狀態統計船在左岸的情況
                    new = State(get.m + i, get.n + j, 1)
                    child.append(new)
                    # print(2)
                # 優先級: not>and>true。如果狀態不安全或者要拓展的節點與當前節點的父節點狀態一致。
                if not safe(new) or back(new, get):  # 狀態非法或new折返了
                    child.pop()
                # 如果要拓展的節點滿足以上情況，將他的父親節點設為當前節點，計算f，並對open_list排序
                else:
                    new.father = get
                    new.g = get.g + 1  # 與起點的距離
                    new.f = get.g + h(get)  # f = g + h
                    open_list.append(new)
                    # print(len(open_list))
                    open_sort(open_list)
        # 打印open表或closed表
        # for o in open_list:
        #   for o in closed_list:
        #       print(o)
        #       print(o.node)
        #       print(o.father)
        #   print(a)
    return (A)


# 遞迴打印路徑
def printPath(f):
    if f is None:
        return
    printPath(f.father)
    # 注意print()語句放在遞迴前和遞迴後用的區別。放在後實現了倒敘輸出
    print('[%d, %d, ' % (f.node[1], f.node[0]), end='')
    if (f.node[2] == 1):
        print('W]')
    else:
        print('E]')


if __name__ == '__main__':
    # print('有%d個狼, %d個羊, 船容量:%d' % (N, M, K))
    final = A_star(init)
    print("有{}種方案".format(len(final)))
    if final:
        for i in (final):
            print('有解,解為: ')
            printPath(i)
    else:
        print('無解!')
