# tuple
# - 변경 불가(immutable)한 list
# - sequence type ( indexing, slicing, iterable )
# - 주로 함수 반환 값, 안전한 데이터 집합을 만들 때 사용

print("---tuple---")
t1 = () # 비어있는 튜플
t2 = (10) # (int)10과 같음, int/tuple은 변경 불가
t3 = (10, ) # (tuple)(10) 과 같음
t4 = (10, 20)
t5 = 10, 20 # () 생략 -> 자동 packing

print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4, type(t4))
print(t5, type(t5))



# tuple 인덱싱, 읽기전용(수정불가)
tpl = ('a', 'b', 'c', 'd')
print(tpl[0], tpl[1], tpl[2], tpl[3])

# 수정 불가 확인
#tpl[0] = 'A'
#print(tpl[0], tpl[1], tpl[2], tpl[3]) # 변경 안됨, Error

# tuple 슬라이싱
print("---tuple슬라이싱---")
print(tpl[0:2]) # 0, 1만 출력
print(tpl[1::2]) # 1번 인덱스부터 끝까지 2 단위로 끊어서 출력

# tuple unpacking
print('---tuple unpacking---')
q, w, e, r = tpl
print(q, w, e, r)  # a b c d

*r, t = tpl
print(r, t) # ['a', 'b', 'c'] d

# tuple을 이용한 변수 값 할당
print("---tuple을 이용한 변수 값 할당---")
num1, num2 = 100, 200 # ()생략된 tuple
print("num1:", num1) #100
print("num2:", num2) #200

print("---tuple을 이용한 값 교환(swap)---")
num1, num2 = num2 ,num1
print("num1:", num1) #200
print("num2:", num2) #100





