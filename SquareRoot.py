a = float(input("Please enter a number to sqrt: "))
x = a/2 + .00001
running = True
step = 0
while running:
    prevx = x
    x -= (x**2 - a)/(2*x)
    step += 1
    if round(x,5) == round(prevx,5):
        running = False
    else:
        print("Step:" , step , " Guess:" , round(x,5))