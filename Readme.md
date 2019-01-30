## Readme.md

本项目**Python-Noob**参考了《<u>Python For Kids - A Playful Introduction to Programming</u>》(Produced By Jason R. Briggs)按照《<u>PFK lessonplans full</u>》（nostarch.com/pfk) 完成的项目。

### 1. Hello World!

![](lab1-aiming.png)

Activities:

![](lab1-act.png)

[Click Me To See The Lab1](https://github.com/GamerNoTitle/Python-Noob/tree/master/lab1)



### 2. Storing Things in Python

![](lab2-aiming.png)

Activities:

![](lab2-act.png)

[Click Me To See The Lab2](https://github.com/GamerNoTitle/Python-Noob/tree/master/lab2)



### 3. Drawing with the Turtle

![](lab3-aiming.png)

Activities:

![](lab3-act.png)

[Click Me To See The Lab3](https://github.com/GamerNoTitle/Python-Noob/tree/master/lab3)



### 4. Control Statements

![](lab4-aiming.png)

Activities:

![](lab4-act.png)

[Click Me To See The lab4](https://github.com/GamerNoTitle/Python-Noob/tree/master/lab4)



### 5. Control Statements

![](lab5-aiming.png)

Activities:

![](lab5-act.png)

[Click Me To See The Lab5](https://github.com/GamerNoTitle/Python-Noob/tree/master/lab5)



### 6. Code Reuse

![](lab6-aiming.png)

Activities:

![](lab6-act.png)

[Click Me To See The Lab6](https://github.com/GamerNoTitle/Python-Noob/tree/master/lab6)

### 7. Price Question

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

[Click Me To See The Price Question](https://github.com/GamerNoTitle/Python-Noob/tree/master/price-question)

## [Click Me To Back To the Top!](https://github.com/GamerNoTitle/Python-Noob#readmemd)

## END
