##切片相关代码
#!/usr/bin/env python
#-* coding:utf-8 -*
print("本程序用于去除字符串首尾的空格\n")
s=input("现在输入你想要进行操作的字符串\n")
n=1
while (s[n-1:n]==' '):
    s=s[n:]

print("去除首空格后")
print(s)
print("\n")
n=-1
while (n!=0):
    if(s[n]==' '):
        s=s[0:n]
    elif (s[n]!=' '):
        break
print('去除尾空格后\n')
print(s)