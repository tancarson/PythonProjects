import math
x = 20
mantissa , exponent = math.frexp(x)
ln2 = 0.6931471805599451
answer = 0
for i in range (1,50):
    answer += (-1 if i%2 == 0  else 1) * ((mantissa - 1)**i/i)
print(answer + exponent * ln2)