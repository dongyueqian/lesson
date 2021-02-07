"""
    用数组 for循环
"""
import math
def main():

   #     主函数
    money_per_week = 10  # 每周的存入的金额
    increase_money = 10  # 递增的金额
    saving = []  # 账户累计

    for i in range(52):
        saving.append(money_per_week)
        money_per_week += increase_money
        # print("第{}周 存了{}元 账户余额{}".format(i+1, money_per_week, sum(saving)))
        print("第{}周 存了{}元 账户余额{}".format(i+1, money_per_week, math.fsum(saving)))

if __name__ == '__main__':
    main()