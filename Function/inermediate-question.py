
# =========================
x = 5

def fun():
    print(x)
    x = 10

fun()




# =========================
x = 5

def fun():
    global x
    print(x)
    x = 10

fun()
print(x)




# =========================
def fun(x=[]):
    x.append(1)
    print(x)

fun()
fun()
fun()




# =========================
def fun(x, lst=[]):
    lst.append(x)
    return lst

print(fun(1))
print(fun(2))
print(fun(3))




# =========================
x = 10

def fun(a):
    a += 5

fun(x)
print(x)



# =========================
x = [10]

def fun(a):
    a[0] += 5

fun(x)
print(x[0])




# =========================
x = 1

def fun():
    x = 2
    def inner():
        x = 3
        print(x)
    inner()
    print(x)

fun()
print(x)




# =========================
x = 1

def fun():
    global x
    x = 2
    def inner():
        global x
        x = 3
    inner()

fun()
print(x)




# =========================
def fun(n, x=0):
    x += n
    if n == 0:
        return x
    return fun(n-1, x)

print(fun(3))




# =========================
def fun(a, b=[]):
    b.append(a)
    return b

x = fun(1)
y = fun(2)
print(x, y)



# =========================
def fun(n):
    if n == 0:
        return
    fun(n-1)
    fun(n-1)
    print(n, end="")

fun(2)




# =========================
def fun(n):
    if n == 0:
        return 1
    return 2 * fun(n-1)

print(fun(4))




# =========================
def fun(n):
    if n <= 1:
        return 1
    return fun(n-1) + fun(n-1)

print(fun(5))



# =========================
def fun(n):
    if n == 0:
        return 0
    print(n, end="")
    return fun(n//2)

fun(10)



# =========================
def fun(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fun(n//2)
    return 1 + fun(n//2)

print(fun(7))



# =========================
def fun(n):
    if n <= 0:
        return
    print("*", end="")
    fun(n-1)
    fun(n-1)

fun(3)



# =========================
def fun(n):
    if n == 1:
        return 1
    return n * fun(n//2)

print(fun(8))



# =========================
def fun(s):
    if len(s) <= 1:
        return s
    return fun(s[1:]) + fun(s[0])

print(fun("abc"))



# =========================
def fun(n):
    if n == 0:
        return 0
    return fun(n-1) + n + fun(n-1)

print(fun(3))



# =========================
def fun(n):
    if n == 0:
        return ""
    return str(n) + fun(n-2)

print(fun(7))
