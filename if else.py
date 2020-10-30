need_help = input('您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要？')
if need_help == '需要':
    help_type = input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询')
    if help_type == 1:
        print('推荐你去存取款窗口')
    
    elif help_type == 3:
        print('推荐你去咨询窗口')
    
    else:
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        money = float(input('请问您需要兑换多少金加隆呢？'))
        pay_money = str(money * 51.3)
        print('那么，您需要付给我' + pay_money + '人民币。')
        
else:
    print('好的，再见。')