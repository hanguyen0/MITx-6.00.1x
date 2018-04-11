def solution(N):
    # write your code in Python 3.6
    fizz='Fizz'
    buzz='Buzz'
    woof='Woof'
    for num in range(1,N+1):
        if num%3==0 and num%5==0 and num%7==5:
            print(fizz + buzz + woof)
        elif num%3==0 and num%5==0:
            print(fizz + buzz)
        elif num%3==0 and num%7==0:
            print(fizz + woof)
        elif num%5==0 and num%7==0:
            print(buzz + woof)
        elif num%3==0:
            print(fizz)
        elif num%5==0:
            print(buzz)
        elif num%7==0:
            print(woof)
        else:
            print(num)


solution(24)
