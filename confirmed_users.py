unconfirmed_users = ['Alice', 'brain', 'candace']
confirmed_users = []   # 首先创建未验证的用户列表

while unconfirmed_users:   # 不断循环，直到列表为空
    current_user = unconfirmed_users.pop()   # 以每次一个的方式从列表末尾删除未验证的用户
    print("Verying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())