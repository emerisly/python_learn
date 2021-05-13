# -*- coding: utf-8 -*-
# filename: love.py

# 导入区
import pymysql
import random

# 数据库提取函数 love()
def love():
    conn = pymysql.connect(
        host="你的数据库地址",
        port=3306,  #端口号, 默认为3306
        user="用户名",
        password="密码",
        db="jiawulab",   # 填写你设置的数据库名称
        charset="utf8")
    cursor = conn.cursor()
    cursor.execute('select reply from love')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return random.choice(data)[0]

# 主函数
def main():
    # 欢迎语
    print('欢迎来到"情话多说一点"系统！\n您需要什么帮助吗？')
    input('\n帮我想一句情话！按回车键继续。。。')

    while True:
        reply = love()
        print(reply)
        choice = input('\n这句您喜欢吗？喜欢请回复"y"! 不喜欢，直接回车键，我再帮你找一句:')
        if choice == 'y':
            print('真开心，我能帮到您！\n\n系统关闭，下次再见！')
            break

if __name__ == '__main__':
    main() # -*- coding: utf-8 -*-
# filename: love.py

# 导入区
import pymysql
import random

# 数据库提取函数 love()
def love():
    conn = pymysql.connect(
        host="你的数据库地址",
        port=3306,  #端口号, 默认为3306
        user="用户名",
        password="密码",
        db="jiawulab",   # 填写你设置的数据库名称
        charset="utf8")
    cursor = conn.cursor()
    cursor.execute('select reply from love')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return random.choice(data)[0]

# 主函数
def main():
    # 欢迎语
    print('欢迎来到"情话多说一点"系统！\n您需要什么帮助吗？')
    input('\n帮我想一句情话！按回车键继续。。。')

    while True:
        reply = love()
        print(reply)
        choice = input('\n这句您喜欢吗？喜欢请回复"y"! 不喜欢，直接回车键，我再帮你找一句:')
        if choice == 'y':
            print('真开心，我能帮到您！\n\n系统关闭，下次再见！')
            break

if __name__ == '__main__':
    main()