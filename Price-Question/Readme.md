## Readme.md

### Price Question

问题如下：

```
用Python语言实现：
使用10吨水以下每吨水收取1.5元；使用50吨以下，超过10吨的部分每吨3元；使用超过50吨水，超过部分每吨水收取4元

E.G.
Input：100
Output:335元
```



具体代码如下

```python
def cal():
    q=float(input("请输入用水（吨）："))
    if q<0:
        print("Error:Invalid Number!")
    elif q>=0 and q<=10:
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
```