import os
import sys
import time
from getpass import getpass
from colorama import Fore, Style

from service.role_service import RoleService
from service.user_service import UserService
from service.news_service import NewsService

__user_service = UserService()
__news_service = NewsService()
__role_service = RoleService()

while True:
    os.system("clear")
    print(Fore.LIGHTBLUE_EX, "\n\t===========================")
    print(Fore.LIGHTBLUE_EX, "\n\t新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t===========================")
    print(Fore.LIGHTBLUE_EX, "\n\t1.登陆系统")
    print(Fore.LIGHTBLUE_EX, "\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt = input("\n\t请输入操作编号:")
    if opt == "1":
        # 用户登陆
        os.system("clear")
        username = input("\n\t请输入用户名:")
        password = getpass("\n\t请输入密码:")
        result = __user_service.login(username, password)

        if result:
            # 登陆成功，查询用户角色
            role = __user_service.search_user_role(username)
            if role == "管理员":
                # 进入管理员操作界面
                while True:
                    os.system("clear")
                    print(Fore.LIGHTGREEN_EX, "\n\t1.新闻管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.用户管理")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登陆")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t请输入操作编号:")
                    if opt == "back":
                        break
                    elif opt == "exit":
                        os.system("clear")
                        sys.exit()
                    elif opt == "1":
                        # 进入新闻管理界面
                        while True:
                            os.system("clear")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.审核新闻")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t请输入操作编号:")
                            if opt == "back":
                                break
                            elif opt == "1":
                                # 进入新闻审核界面
                                page = 1
                                while True:
                                    os.system("clear")
                                    # 判断是否有新闻，没有则提示一下，返回上一层
                                    news_list = __news_service.search_unreview_list(page)
                                    if not news_list:
                                        print(Fore.LIGHTBLUE_EX, "\n\t目前没有待审批的新闻(3秒后返回上一层)")
                                        time.sleep(3)
                                        break
                                    total_page = __news_service.search_unreview_count_page()
                                    for index in range(len(news_list)):
                                        news = news_list[index]
                                        print(Fore.LIGHTBLUE_EX, "\n\t{0}\t{1}\t{2}\t{3}".format(index+1, news[1], news[2], news[3]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t{0}/{1}".format(page, total_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作编号:")
                                    if opt == "back":
                                        break
                                    elif opt == "prev":
                                        if page > 1:
                                            page -= 1
                                    elif opt == "next":
                                        if page < total_page:
                                            page += 1
                                    elif opt.isdigit() and int(opt) in range(1, 11):
                                        news_id = news_list[int(opt)-1][0]
                                        __news_service.update_unreview_news(news_id)
                            elif opt == "2":
                                # 进入删除新闻界面
                                page = 1
                                while True:
                                    os.system("clear")
                                    # 判断是否有新闻，没有则提示一下，返回上一层
                                    news_list = __news_service.search_list(page)
                                    if not news_list:
                                        print(Fore.LIGHTBLUE_EX, "\n\t目前没有新闻(3秒后返回上一层)")
                                        time.sleep(3)
                                        break
                                    total_page = __news_service.search_unreview_count_page()
                                    for index in range(len(news_list)):
                                        news = news_list[index]
                                        print(Fore.LIGHTBLUE_EX, "\n\t{0}\t{1}\t{2}\t{3}".format(index+1, news[1], news[2], news[3]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t{0}/{1}".format(page, total_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作编号:")
                                    if opt == "back":
                                        break
                                    elif opt == "prev":
                                        if page > 1:
                                            page -= 1
                                    elif opt == "next":
                                        if page < total_page:
                                            page += 1
                                    elif opt.isdigit() and int(opt) in range(1, 11):
                                        news_id = news_list[int(opt)-1][0]
                                        __news_service.delete_by_id(news_id)
                    elif opt == "2":
                        # 进入用户管理页面
                        while True:
                            os.system("clear")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.添加用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.修改用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t3.删除用户")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t请输入操作编号:")
                            if opt == "back":
                                break
                            elif opt == "1":
                                # 进入用户添加界面
                                os.system("clear")
                                username = input("用户名:")
                                password = getpass("密码:")
                                repassword = getpass("重复密码:")
                                if password != repassword:
                                    print("两次密码输入不一致(3秒后返回)")
                                    time.sleep(3)
                                    continue
                                email = input("邮箱:")
                                role_list = __role_service.search_list()
                                for index in range(len(role_list)):
                                    role = role_list[index]
                                    print(Fore.LIGHTBLUE_EX, "\n\t{0} {1}".format(index+1, role[1]))
                                    print(Style.RESET_ALL)
                                index = input("选择角色编号:")
                                role_id = role_list[int(index)-1][0]
                                __user_service.insert_user(username, password, email, role_id)
                                print("添加用户已完成，3秒后返回")
                                time.sleep(3)
                            elif opt == "2":
                                # 进入用户修改界面
                                page = 1
                                while True:
                                    os.system("clear")
                                    user_list = __user_service.search_list(page)
                                    total_page = __user_service.search_count_page()
                                    for index in range(len(user_list)):
                                        user = user_list[index]
                                        print(Fore.LIGHTBLUE_EX, "\n\t{0}.{1}\t{2}\t{3}".format(index+1, user[1], user[2], user[3]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t{0}/{1}".format(page, total_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作编号:")
                                    if opt == "back":
                                        break
                                    elif opt == "prev":
                                        if page > 1:
                                            page -= 1
                                    elif opt == "next":
                                        if page < total_page:
                                            page += 1
                                    elif opt.isdigit() and int(opt) in range(1, 11):
                                        user_id = user_list[int(opt)-1][0]
                                        os.system("clear")
                                        username = input("用户名:")
                                        password = getpass("密码:")
                                        repassword = getpass("重复密码:")
                                        if password != repassword:
                                            print("两次密码输入不一致(3秒后返回)")
                                            time.sleep(3)
                                            continue
                                        email = input("邮箱:")
                                        role_list = __role_service.search_list()
                                        for index in range(len(role_list)):
                                            role = role_list[index]
                                            print(Fore.LIGHTBLUE_EX, "\n\t{0} {1}".format(index+1, role[1]))
                                            print(Style.RESET_ALL)
                                        index = input("选择角色编号:")
                                        role_id = role_list[int(index)-1][0]
                                        __user_service.update_by_id(user_id, username, password, email, role_id)
                                        print(Fore.LIGHTGREEN_EX, "用户修改完成，3秒后返回")
                                        time.sleep(3)
                            elif opt == "3":
                                # 进入用户删除界面
                                page = 1
                                while True:
                                    os.system("clear")
                                    user_list = __user_service.search_list(page)
                                    total_page = __user_service.search_count_page()
                                    for index in range(len(user_list)):
                                        user = user_list[index]
                                        print(Fore.LIGHTBLUE_EX, "\n\t{0}.{1}\t{2}\t{3}".format(index+1, user[1], user[2], user[3]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t{0}/{1}".format(page, total_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作编号:")
                                    if opt == "back":
                                        break
                                    elif opt == "prev":
                                        if page > 1:
                                            page -= 1
                                    elif opt == "next":
                                        if page < total_page:
                                            page += 1
                                    elif opt.isdigit() and int(opt) in range(1, 11):
                                        user_id = user_list[int(opt)-1][0]
                                        __user_service.delete_by_id(user_id)
                                        print(Fore.LIGHTGREEN_EX, "\n\t用户删除完成，3秒后返回")
                                        time.sleep(3)
            elif role == "新闻编辑":
                # 进入新闻编辑操作界面
                os.system("clear")
                print(Fore.LIGHTRED_EX, "\n\t新闻编辑功能正在开发中......")
                time.sleep(3)
        else:
            # 登陆失败
            os.system("clear")
            print("\n\t登陆失败(3秒后返回)")
            time.sleep(3)
    elif opt == "2":
        os.system("clear")
        sys.exit()
