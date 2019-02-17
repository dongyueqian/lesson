
 #   周存钱计算器

def main():
   #     主函数

    money_per_week = 10  # 每周的存入的金额
    num_week = 1  # 记录周数
    increase_money = 10  # 递增的金额
    total_week = 52  # 总共的周数
    saving = 0  # 账户累计

    while num_week <= total_week:


        saving += money_per_week
        #输出第几周、每周存的钱数、每周的账户余额
        print("第{}周 存了{}元 账户余额{}".format(num_week,money_per_week,saving))
        num_week += 1
        money_per_week +=increase_money

if __name__ == '__main__':
    main()
