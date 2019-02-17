"""
    单独的存钱函数
"""
import math
def saving_money(money_per_week,increase_money,sum_weeks):
    maonry_list = []
    for i in range(sum_weeks):
        maonry_list.append(money_per_week)
        saving = math.fsum(maonry_list)
        money_per_week += increase_money
    return saving

def main():

   #     主函数
    money_per_week = float(input("每周的存入的金额: ")) # 每周的存入的金额
    increase_money = float(input("每周的递增的金额: "))  # 递增的金额
    sum_weeks = int(input("总周数： "))                 #总周数
    # saving = []  # 账户累计
    saving = saving_money(money_per_week,increase_money,sum_weeks)
    print("总存款为：",saving)

if __name__ == '__main__':
    main()