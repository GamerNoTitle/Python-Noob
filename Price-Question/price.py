def cal():
    q=float(input("请输入用水（吨）："))
    if q<=10:
        price=q*1.5
        print(price);print("元")
    elif q>10 and q<=50:
       price=3*q-15
       print(price);print("元")
    elif q>50:
       price=4*q-65
       print(price);print("元")
x=0
while x==0:
    cal()