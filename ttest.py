import random

sign1 = ""
x = ["н", "г", "р", "о", "т", "ь"]

z = random.randint(3, 10)
for i in range(10):
    sign = random.choice(x)
    sign1 += sign

print(sign1)
