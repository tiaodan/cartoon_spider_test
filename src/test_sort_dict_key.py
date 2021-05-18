
def dictionairy():
    # 声明字典
    key_value = {}

    # 初始化  --》key 是str 排序正确
    # key_value[2] = 56
    # key_value[1] = 2
    # key_value[5] = 12
    # key_value[4] = 24
    # key_value[6] = 18
    # key_value[3] = 323
    # key_value[11] = 323

    # 初始化 --》key 是int 排序正确
    key_value['2'] = 56
    key_value['1'] = 2
    key_value['5'] = 12
    key_value['4'] = 24
    key_value['6'] = 18
    key_value['3'] = 323
    key_value['11'] = 323

    print("按键(key)排序:")

    # sorted(key_value) 返回重新排序的列表
    # 字典按键排序
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")
        print(type(key_value[i]))


def main():
    # 调用函数
    dictionairy()


# 主函数
if __name__ == "__main__":
    main()