salary = 80
if salary <= 500:
    print('欢迎进入史塔克穷人帮前三名')
    if salary > 100:
        print('请找弗瑞队长加薪')
    else:
        print('恭喜您荣获“美元队长”称号！')
else:
    if salary <= 1000:
        print('祝贺您至少可以温饱了。')
    elif salary <= 20000:
        print('您快比钢铁侠有钱了！')
    else:
        print('您是不是来自于瓦坎达国？')
print('程序结束')
    
