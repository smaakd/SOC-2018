#! /usr/bin/env python
# _*_ coding:utf-8 _*_
import sys              
user_info=open('userinfo.txt','a+')#以追加可读写模式打开用户信息存储文件userinfo.txt
lock_info=open('lock.txt','a+')    #以追加可读写模式打开锁定信息文件
user=raw_input('请输入用户名:')    #输入用户名
line=lock_info.readlines()         #将锁定账号信息赋值给列表line
user_list=user_info.readlines()    #将用户账号信息赋值给列表user_list
i=0
b=0
n=1
while i<len(line):                 #循环读取列表line中的锁定账号信息
  if line[i].strip()==user:        #去掉列表中的空格,换行符等特殊字符,然后与输入的用户名比较
     print ('你的账号被锁定')      #输入的用户名在锁定列表中，则提示锁定，退出程序
     sys.exit()                    
  else:                            #i 加一，循环读取列表的账号信息
     i+=1
while b<len(user_list):             #循环读取用户的账号和密码信息
  username=user_list[b]              #读取用户账号
  password=user_list[b+1]            #读取用户密码
  b=b+2                              #读取下一个用户信息
  while username.strip()==user:      #用户输入账号存在在列表中，则验证密码
    passwd=raw_input('请输入密码:')  #输入密码
    if password.strip()==passwd:     #密码验证
         print "欢迎登陆"             #验证成功，打印欢迎信息
         sys.exit()
    else:
         if n<3:                      #密码错误，重新输入密码，上限为3次
           print "密码错误,剩余尝试次数:",3-n
           n+=1
           continue
         else:                        #密码错误超过三次，将账号写入锁定文件中
           lock_info.write('%s\n'%user)
           print "密码错误太多,你的账号被锁定啦"
           sys.exit()

print "该用户不存在"                #该账号不存在，则进行注册
while 1>0:                          #该循环的作用是在输入非y/n时，让用户重新选择
 choice=raw_input("你是否要注册（y/n）:")  
 if choice=="y":                      #用户选择注册，将用户输入的用户名和密码写入用户信息存储文件中
   username1=raw_input("请输入用户名:")
   passwd1=raw_input("请输入密码:")
   user_info.write("%s\n"%username1)
   user_info.write("%s\n"%passwd1)
   print "恭喜你完成注册"
   su=raw_input("想要惊喜吗(y/n):")   #调用love.py的代码
   for y in range(15, -15, -1):
     l_sStr=""
     for x in range(-30, 30):
       if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0:
         l_sStr+= 'PYTHON!'[(x-y)%7]
       else:
          l_sStr+= " "
     print l_sStr
   sys.exit()
   user_info.close()          #关闭文件，确保写入的内容保存到文件中
 elif choice=="n":             #不注册，退出
   sys.exit()
 else:
   print "请输入'y'或者'n'"     #如果用户输入的内容非n或者y，则让用户重新输入
   continue   
