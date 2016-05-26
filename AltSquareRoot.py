def factorial(x):
    answer = 1
    for i in range(2,x+1):
        answer *= i
    return answer

x = 5
answer = 1
for i in range(1,50):
    answer += x**i/factorial(i)
print(answer)