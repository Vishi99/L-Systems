import turtle as t

def Produce(depth):
    str = "A"
    for i in range(depth):
        temp = ""
        for char in str:
            if char == "A":
                temp = temp + "B-A-B"
            elif char == "B":
                temp = temp + "A+B+A"
            else:
                temp = temp + char
        str = temp
    return str

def Draw(prod_str, leng):
    t.tracer(0, 0)
    for ele in prod_str:
        if (ele == "A" or ele == "B"):
            t.fd(leng)
        elif ele == "+":
            t.lt(60)
        elif ele == "-":
            t.rt(60)
    t.update()

def init_turtle():
    t.speed(speed = 0)
    t.up()
    t.goto(-250, -250)
    t.down()

def main():
    depth = 10
    leng = 0.5
    init_turtle()
    prod_str = Produce(depth)
    print(prod_str)
    Draw(prod_str, leng)
    t.exitonclick()

main()
