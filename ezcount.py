 # -*- coding: GB2312 -*- 
 #这些虚拟变量是为了下个版本可以保存状态，就像反序列化一样
from msilib import sequence
from zipapp import ZipAppError


def help():#帮助函数
    print('''1.cj 变量名=值 来创建一个变量\n2.tq 变量名 来提取变量\n3,setoutall 来输出每一步的值\n4,zx 变量名=表达式来执行python语法标准的运算式\n5,退出程序输入eixt''')
    return 0
def cshsz(sl):#初始化数组来为存放变量而准备
    global blm
    global blz
    blm = ['name is there']
    blz = ['numerical value is here']
    global stack
    global setcoutall
    setcoutall=0#设置输出每步所有变量值
    stack=1
    while sl>0:
        sl=sl-1
        blm.append('name is there')
        blz.append('numerical value is here')
    return 0
def clbds(cmda):#处理传入cmd的表达式
    xh=1
    while xh<stack:
        cmda=str(cmda).replace(blm[xh],"blz[*r_e_p*]")
        cmda=str(cmda).replace(("*r_e_p*"),str(xh))
        xh=xh+1
    return cmda
def coutall():#输出所有变量
    global blm
    global blz
    xh=1
    while xh<stack+1:
        print(blm[xh]+"="+blz[xh])
        xh=xh+1
    return 0
def cjbl(name,price):#创建虚拟变量
    global stack
    global blm
    global blz
    global stack
    blm[stack]=name
    blz[stack]=price
    print('\033[32mnormal\033[0m'+'  '+blm[stack]+'  ''已被创建')
    stack=stack+1
    return 0
def tq(zhi):#提取虚拟变量值
    global blm
    global blz
    b=1
    while b<cshsl+1:
        if blm[b]==zhi:
            print(blm[b]+'='+blz[b])
            return 1
        b=b+1
    print('\033[31mezcount:not found\033[31m')
    return 0
def com1jx(command):#用于解析命令返回变量值与名称
    xr=0
    b=0
    fir=0
    global wname
    global wprice
    wname=''
    wprice=''
    for a in command:   
        b=b+1            
        if b>3:
            if a=='=':
               xr=1
               fir=0
            if xr==0:
                wname+=a
            if fir==1:
                wprice+=a
            if xr==1:
               fir=1
    return 0
def cmd(cmdc):#调用eval计算
    global blm
    global blz
    global stack
    global setcoutall
    sq=0
    sh=0
    xh=1
    blmz=''
    cmda=''
    for a in cmdc:
        if sh==1:
            cmda=cmda+a
        if a=='=':
            sq=1
            sh=1
        if sq==0:
            blmz=blmz+a
    while xh<stack+1:
        if blm[xh]==blmz:
            cmdz=''
            cmdz=clbds(cmda)
            print("\""+cmdz+"\"将会被执行")
            blz[xh]=str(eval(cmdz))
            hx=10000000
        xh=xh+1 
    if setcoutall==1:
        coutall()
        return 0
#以下开始为主程序
eix=0
print('''\033[31mezcount v0.1\033[0m''')
print("ezcount:如果你第一次运行程序，不知道如何使用,可以输入help来查看教程\n你希望初始化多少个变量空间(回撤默认20)")
cshsl=int(input('ezcount:'))
if cshsl=='':
    cshsl=20
cshsz(cshsl)
print('\033[32mezcount:normal\033[0m')
while eix<1:
    command=input('ezcount:')
    if command=='help':
        help()
        command='nop'
    if 'cj' in command:#创建和给变量赋值
        com1jx(command)
        cjbl(wname,wprice)
        command='nop'
    if 'tq' in command:
        dqcs=command[3:]
        tq(dqcs)
    if 'zx' in command:
        cmdcs=command[3:]
        cmd(cmdcs)
        command='nop'
    if command=='eixt':
        eix=2
    if command=='setoutall':
        setcoutall=1
        print('现在计算的每一步都会输出值')
