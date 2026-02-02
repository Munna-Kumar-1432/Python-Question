# =========================

x = 10

def fun():
    x = 5
    print(x)

fun()
print(x)




# =========================
x = 10

def fun():
    global x
    x = 5

fun()
print(x)




# =========================
count = 0

def fun():
    global count
    count += 1

fun()
fun()
fun()

print(count)



# =========================
x = 3

def fun():
    x = x + 2
    print(x)

fun()



# =========================
x = 3

def fun():
    global x
    x = x + 2

fun()
print(x)




# =========================
total = 0

def fun(n):
    global total
    if n == 0:
        return
    total += n
    fun(n-1)

fun(3)
print(total)



# =========================
x = 5

def fun():
    x = 10
    def inner():
        print(x)
    inner()

fun()




# =========================
x = 5

def fun():
    global x
    x = 10
    def inner():
        x = 20
        print(x)
    inner()

fun()
print(x)



# =========================
x = 1

def fun(n):
    global x
    if n == 0:
        return
    x += n
    fun(n-1)

fun(3)
print(x)



# =========================
x = 2

def fun(n):
    if n == 0:
        return 1
    return x * fun(n-1)

print(fun(3))



# =========================
x = 2

def fun():
    x = 3
    return x

print(fun())
print(x)




# =========================
x = 0

def fun(n):
    global x
    if n == 0:
        return
    x += 1
    fun(n-1)

fun(5)
print(x)



# =========================
x = 100

def fun():
    print(x)

def change():
    x = 50
    fun()

change()


# =========================
x = 5

def fun():
    global x
    x = x * 2

def run():
    x = 3
    fun()
    print(x)

run()
print(x)



# =========================
x = 1

def fun(n):
    global x
    if n <= 1:
        return
    x *= n
    fun(n-1)

fun(4)
print(x)


# =========================
def fun(n):
    if n == 0:
        return
    print(n, end=" ")
    fun(n-1)

fun(3)


# =========================
def fun(n):
    if n == 0:
        return
    fun(n-1)
    print(n, end=" ")

fun(3)



# =========================
def fun(n):
    if n <= 1:
        return 1
    return n * fun(n-1)

print(fun(4))



# =========================
def fun(n):
    if n == 0:
        return 0
    return n + fun(n-1)

print(fun(4))



# =========================
def fun(n):
    if n == 0:
        return
    print(n)
    fun(n-2)

fun(5)



# =========================
def fun(n):
    if n == 0:
        return 0
    return fun(n//10) + n%10

print(fun(123))



# =========================
def fun(n):
    if n <= 1:
        return n
    return fun(n-1) + fun(n-2)

print(fun(5))



# =========================
def fun(s):
    if len(s) == 0:
        return ""
    return fun(s[1:]) + s[0]

print(fun("abc"))



# =========================
def fun(a, b):
    if b == 0:
        return a
    return fun(b, a % b)

print(fun(12, 8))




# =========================
def fun(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fun(n//2)
    return 2 * fun(n//2)

print(fun(5))





# =========================
def fun(n):
    if n < 10:
        return n
    return fun(n//10)

print(fun(9876))



# =========================
count = 0

def fun(n):
    global count
    if n == 0:
        return
    count += 1
    fun(n-1)

fun(5)
print(count)



# =========================
def fun(x):
    if x == 0:
        return 0
    print(x, end="")
    fun(x-1)
    print(x, end="")

fun(3)




# =========================
def square(x):
    return x*x

def fun(n):
    if n == 0:
        return 0
    return square(n) + fun(n-1)

print(fun(3))




# =========================
def fun(s):
    if len(s) <= 1:
        return s
    return fun(s[1:-1])

print(fun("abcdef"))



# =========================
def fun(n):
    if n == 0:
        return
    fun(n-1)
    print(n, end="")
    fun(n-1)

fun(3)



# =========================
def fun(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return fun(n//2)
    return 1 + fun(n-1)

print(fun(7))



# =========================
def fun(n):
    if n <= 1:
        return n
    return fun(n-1) * fun(n-2)

print(fun(5))


# =========================
def fun(n):
    if n == 0:
        return 1
    return n + fun(n-1) + fun(n-2)

print(fun(4))


# =========================
def fun(s):
    if s == "":
        return 0
    return 1 + fun(s[1:-1])

print(fun("abcdef"))



# =========================
def fun(n):
    if n < 10:
        return n
    return fun(n//10) + fun(n%10)

print(fun(1234))


# =========================
def fun(n):
    if n == 0:
        return ""
    return fun(n//2) + str(n%2)

print(fun(6))



# =========================
def fun(a, b):
    if b == 0:
        return 0
    return a + fun(a, b-1)

print(fun(3, 4))


# =========================
def fun(n):
    if n == 1:
        return 1
    return fun(n//2) + fun(n//2)

print(fun(8))


# =========================
def fun(n):
    if n == 0:
        return 0
    print(n, end="")
    return fun(n-2)

fun(7)
