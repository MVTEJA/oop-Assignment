#1.

def maxi(a , b):
    return a if(a >= b) else  b

print(maxi(5 , 10))

#2.

def numbergame(k):
    pass


#3.

def numbergame(k):
    if (k % 3 == 0):
        return "number"
#4.

def numbergame(k):
    if (k % 5 == 0):
        return "Game"

#5.

def numbergame(k):
    if (k % 5 == 0 and k % 3 == 0):
        return "numberGame"

#6.

def numbergame(k):
    if (k % 5 == 0 and k % 3 == 0):
        return "numberGame"
    else :
        return k
#7.

def check(speed):
    pass

#8.

def check(speed):
    if(speed < 70):
        print("OK")

#9.

def check(speed):

    sum = 0

    if(speed < 70):
        print("OK")
    else:
        while(speed <= 70):
            speed = speed - 5
            sum = sum + 1

    return sum

#10.

def check(speed):
    sum = 0

    if (speed < 70):
        print("OK")
    else:
        while (speed <= 70):
            speed = speed - 5
            sum = sum + 1

            if(sum > 12):
                print("License suspended")


    return sum

#11.

def showNumbers(limit):

    for i in range(0 , limit + 1):
        if(i % 2 == 0):
            print(i + "even")
        else:
            print(i + "odd")

#12.

def showSigns(rows):

    for i in range(1 , rows+1):
        for j in range(i):
            print("&" , end = "")
        print("\n")


#13.

def prime(max):
    for x in range(max):
        for y in range(2 , x):
            if(x%y == 0):
                break
        else:
            print(x)














