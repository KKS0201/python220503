# DemoTuple.py

a =  {1,2,3,3}
print(a)
print(type(a))
b = {3,4,4,5}
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Tuple 연습
tp = (1,2,3)
print(type(tp))
print(len(tp))
print(tp[0])

#함수 정의
def time(a,b):
    return a+b,a*b

#함수 호출
result = time(3,4)
print(result)
print(result[0])
print(result[1])