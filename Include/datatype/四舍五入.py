num=4.56
print(round(num))
# 遇到 x.5的数字，如果X是偶数取得是x，如果X是奇数，取得的是X+1！(离偶数最近，取最近的偶数)

#计算剩余
num=eval(input("请输入金额（单位：分）："))
print("剩下的金额（单位：分）：",num % 10)
print("花去的金额（单位：分）：",(num // 10) * 10)


#获取分
money = eval(input("请输入金额："))
min = (money * 10 - int(money * 10)) / 10
print("输出的分：",min)

