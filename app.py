import os
import sys
import time
from getpass import getpass
from colorama import Fore, Style

from service.role_service import RoleService
from service.type_service import TypeService
from service.user_service import UserService
from service.news_service import NewsService

__user_service = UserService()
__news_service = NewsService()
__role_service = RoleService()
__type_service = TypeService()

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
                                        # 查询对应新闻信息
                                        news = __news_service.search_cache(news_id)
                                        # TODO 通过content_id从MongoDB获取正文信息，放入news中，待完善
                                        content = "1111111"
                                        news.append(content)
                                        # 将审核通过的信息缓存到redis中
                                        __news_service.cache_news(news)
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
                                        __news_service.cache_delete(news_id)
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
                while True:
                    os.system("clear")
                    print(Fore.LIGHTGREEN_EX, "\n\t1.发表新闻")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.编辑")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登陆")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t请输入操作编号:")
                    if opt == "exit":
                        sys.exit()
                    elif opt == "back":
                        break
                    elif opt == "1":
                        # 进入发表新闻界面
                        os.system("clear")
                        title = input("\n\t新闻标题:")
                        editor_id = __user_service.search_by_username(username)[0]
                        type_list = __type_service.search_list()
                        for index in range(len(type_list)):
                            news_type = type_list[index]
                            print(Fore.LIGHTBLUE_EX, "\n\t{0} {1}".format(index+1, news_type[1]))
                            print(Style.RESET_ALL)
                        index = input("\n\t选择新闻类型:")
                        type_id = type_list[int(index)-1][0]
                        # TODO 新闻内容id，这里需要用到MongoDB，后面再完善
                        content_id = 100
                        is_top = input("\n\t是否置顶(0-5):")
                        __news_service.insert(title, editor_id, type_id, content_id, is_top)
                        print(Fore.LIGHTGREEN_EX, "\n\t保存完成，3秒后返回")
                        time.sleep(3)
                    elif opt == "2":
                        # 进入新闻编辑界面
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
                                news = __news_service.search_by_id(news_id)
                                print("\n\t新闻原标题:{}".format(news[0]))
                                title = input("\n\t请输入标题:")
                                print("\n\t新闻原类型:{}".format(news[1]))
                                type_list = __type_service.search_list()
                                for index in range(len(type_list)):
                                    news_type = type_list[index]
                                    print(Fore.LIGHTBLUE_EX, "\n\t{0} {1}".format(index+1, news_type[1]))
                                    print(Style.RESET_ALL)
                                index = input("\n\t选择新闻类型:")
                                type_id = type_list[int(index)-1][0]
                                # TODO 修改新闻内容
                                content_id = 100
                                print("\n\t原置顶级别:{}".format(news[2]))
                                is_top = input("\n\t置顶级别(0-5):")
                                is_commit = input("\n\t是否提交?(Y/N):")
                                if is_commit == "Y" or is_commit == "y":
                                    __news_service.update_by_id(news_id, title, type_id, content_id, is_top)
                                    print("\n\t保存成功，3秒后自动返回")
                                    time.sleep(3)
        else:
            # 登陆失败
            os.system("clear")
            print("\n\t登陆失败(3秒后返回)")
            time.sleep(3)
    elif opt == "2":
        os.system("clear")
        sys.exit()
