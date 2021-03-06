# function2.py
# 함수 내부에서 이름 해석(LGB)

from re import X


x = 2
def func1(a) :
    return a+x

#호출
print(func1(1))

#함수정의
def func2(a):
    x = 5
    return a + x

#호출
print(func2(1))

#기본값
def times(a=10,b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드 인자
def connectURL(server,port):
    strURL = "http://"+ server + ":" + port
    return strURL

print(connectURL("credu.com","80"))
print(connectURL(port="8080",server="credu.com"))


#가변인자(가변적인 상황)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result
#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))


#람다 함수 : 간결하게 함수를 정의
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(3))
print(globals())

