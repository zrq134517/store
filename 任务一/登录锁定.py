m=3
while  m>0:
  print("剩余登陆次数：",m)
  print("输入用户名：")
  yhm=str(input())
  print("输入密码：")
  ma=str(input())
  if yhm=="root":
    print()
  else:
     print("登陆失败")
     m=m-1
     if m == 0:
       print("重复3次错误，账号已锁定")
     continue
  if  ma=="admin":
    print("登陆成功")
    break
  else:
     print("登陆失败")
     m=m-1
  if m==0:
    print("重复3次错误，账号已锁定")