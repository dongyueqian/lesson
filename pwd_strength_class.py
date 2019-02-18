"""
    密码强度
    保存密码到txt文件
    规则：
    1、密码长度不小于8
    2、密码必须含有数字
    3、密码必须含有字母

    用面向对象思想

    (待实现：密码必须有大写字母、不能有中文和特殊符号、读取文件最后一行)
"""

class PasswordTool:
    # 密码设置、判断工具类

    def __init__(self,password):
        self.password = password
        self.pwd_strength = 0

    def pwd_number_check(self):
        """
            判断是否含有数字
        """
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def pwd_letter_check(self):
        """
            判断是否含有字母
        """
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter

    def password_set(self):
        """
            密码强度判断
        """
        # 长度不小于8
        if len(self.password) >= 8:
            self.pwd_strength += 1
        else:
            print("密码长度小于8！")
        # 含有数字

        if self.pwd_number_check():
            self.pwd_strength += 1
        else:
            print("密码不含数字！")

        # 含有字母
        if self.pwd_letter_check():
            self.pwd_strength += 1
        else:
            print("密码不含字母！")

class FileTool:
    # 文件操作工具类

    def __init__(self,filepath):
        self.filepath = filepath

    def file_write(self,line):
        f = open(self.filepath,'a')
        f.write(line)
        f.close()

    def file_read(self):
        f = open(self.filepath,'r')
        lines = f.read()
        f.close()
        return lines

def main():
    """
        主函数
    """
    #允许用户输入3次
    times = 3
    filepath = '/Users/dongyueqian/Desktop/password.txt'
    # 实例化一个文件工具类对象
    file_tool = FileTool(filepath)

    while times > 0:

        password = input("请输入密码： ")

        #实例化一个密码工具类对象
        password_tool = PasswordTool(password)
        password_tool.password_set()

        # 把密码写入文件
        line = '密码：{}, 强度：{}\n'.format(password,password_tool.pwd_strength)
        file_tool.file_write(line)

        if password_tool.pwd_strength == 3:
            print("密码设置成功！")
            break
        else:
            print("密码强度不合格，请重新输入！")
            times -= 1

        print() #打印空行

    if times <=0:
        print("您的次数已用完，密码设置失败！")

    lines = file_tool.file_read()
    print(lines)

if __name__ == '__main__':
    main()
