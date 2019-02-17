#variables : A
#constants: +, -
#axiom : A-A-A
#rules : (A → A+A-A+A)

import turtle as t

def init_turtle():
    t.speed(speed=0)
    t.up()
    t.goto(-100, -100)
    t.lt(60)
    t.down()

def Produce(depth):
    str = "A-A-A"
    for i in range(depth):
        temp = ""
        for char in str:
            if char == "A":
                temp = temp + "A+A-A+A"
            else:
                temp = temp + char
        str = temp
    return str

def Draw(prod_str, leng):
    t.tracer(0, 0)
    for ele in prod_str:
        if ele == "A":
            t.fd(leng)
        elif ele == "+":
            t.lt(60)
        elif ele == "-":
            t.rt(120)
    t.update()

def main():
    depth = 6
    leng = 0.5
    init_turtle()
    prod_str = Produce(depth)
    print(prod_str)
    Draw(prod_str, leng)
    t.exitonclick()

main()
