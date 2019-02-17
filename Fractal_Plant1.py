#variables : X F
#constants : + − [ ]
#axiom : X
#rules : (X → F+[[X]-X]-F[-FX]+X), (F → FF)
#angle : 20deg

import turtle as t

def init_turtle():
    t.speed(speed = 0)
    t.color("green")
    t.up()
    t.goto(-250, -250)
    t.lt(60)
    t.down()

def move_turtle(pos):
    t.up()
    t.goto(pos[0][0], pos[0][1])
    t.setheading(pos[1])
    t.down()

def Produce(depth):
    str = "X"
    for i in range(depth):
        temp = ""
        for char in str:
            if char == "X":
                temp = temp + "F+[[X]-X]-F[-FX]+X"
            elif char == "F":
                temp = temp + "FF"
            else:
                temp = temp + char
        str = temp
    return str

def Draw(prod_str, leng):
    stack = []
    t.tracer(0, 0)
    for ele in prod_str:
        if ele == "F":
            t.fd(leng)
        elif ele == "+":
            t.lt(20)
        elif ele == "-":
            t.rt(20)
        elif ele == "[":
            stack.append((t.pos(), t.heading()))
        elif ele == "]":
            move_turtle(stack.pop(len(stack) - 1))
    t.update()

def main():
    depth = 7
    leng = 2
    init_turtle()
    prod_str = Produce(depth)
    print(prod_str)
    Draw(prod_str, leng)
    t.exitonclick()

main()
