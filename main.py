import turtle

# L-system
axiom = "X"
chr_1, rule_1 = "X", "F−[[X]+X]+F[+FX]−X"
chr_2, rule_2 = "F", "FF"
step = 12
angle = 25
gens = 6

# all screen parameters
WIDTH, HEIGHT = 1920, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(30 * WIDTH, 30 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)

# all turtle settings
painter = turtle.Turtle()
painter.pensize(1)
painter.speed("fastest")
painter.setpos(-WIDTH // 5, -HEIGHT // 5)
painter.color('green')


# X  -->  F−[[X]+X]+F[+FX]−X  -->  FF−[[F−[[X]+X]+F[+FX]−X]+F−[[X]+X]+F[+FX]−X]+FF[+FFF−[[X]+X]+F[+FX]−X]−F−[[X]+X]+F[+FX]−X ... ETC
def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else rule_2 if chr == chr_2 else chr for chr in axiom])


# saves the new value of the axiom.
# process generations
def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


# text
turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, -HEIGHT // 2 + 60)
turtle.clear()
turtle.write(f'Generation: {gens}', font=("Arial", 20, "normal"))

axiom = get_result(gens, axiom)

stack = []

for chr in axiom:
    if chr == chr_1 or chr == chr_2:
        painter.forward(step)
    elif chr == '+':
        painter.right(angle)
    elif chr == '-':
        painter.left(angle)
    elif chr == '[':
        stack.append((painter.position(), painter.heading()))  # after the opening bracket saves the position
    elif chr == ']':
        pos, head = stack.pop()  # after the closing bracket returns to the saved position and continues to work there
        painter.penup()
        painter.goto(pos)
        painter.setheading(head)
        painter.pendown()

turtle.Screen().exitonclick()
