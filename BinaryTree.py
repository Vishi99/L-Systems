import turtle as t

def init_turtle():
    t.speed(speed = 0)
    t.up()
    t.lt(90)
    t.goto(0, -150)
    t.down()

def move_turtle(pos):
    t.up()
    t.goto(pos[0][0], pos[0][1])
    t.setheading(pos[1])
    t.down()

def Produce(depth):
    str = "0"
    for i in range(depth):
        temp = ""
        for char in str:
            if char == "1":
                temp = temp + "11"
            elif char == "0":
                temp = temp + "1[0]0"
            else:
                temp = temp + char
        str = temp
    return str

def Draw(prod_str, leng):
    t.tracer(0, 0)
    stack = []
    for ele in prod_str:
        if ele == "1" or ele == "0":
            t.fd(leng)
        elif ele == "[":
            stack.append((t.pos(), t.heading()))
            t.lt(45)
        elif ele == "]":
            move_turtle(stack.pop(len(stack) - 1))
            t.rt(45)
    t.update()

def main():
    depth = 8
    leng = 1
    init_turtle()
    prod_str = Produce(depth)
    print(prod_str)
    Draw(prod_str, leng)
    t.exitonclick()

main()
