# Hallo liebe Kyiv Kindern!
# строка, начинающаяся с "решетки" - это комментарий, тут можно писать что угодно

# subprogram: greatest common divisor (euclidean algorithm)
# 
def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

# subprogram: factorization of a number   
def factor(x):
    f = []
    while x > 1:
        for i in range(2, x + 1):
            if x % i == 0:
                x = x // i
                f.append(i)
                break
            else:
                print("AAAA!")
        print("BBBB!")

        
    return f

def hello_world():
    print("hello world")

print("hello dear!")
y = gcd(32,6)
print(f"greatest common divisor is {y}")
x = 172
multipliers = factor(x)
print(f"factors of x = {x} is {multipliers}")
