n = 3000
inside = 0
for i in range(n):
    for j in range(n):
        if ((i/n)**2 + (j/n)**2 < 1):
            inside += 1
print(inside/(n**2)*4)
#converges very slowly and not random but pretty cool