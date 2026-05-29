# number(숫자형)
# - 정수
# - 실수
# - 복소수

# type(변수명 | 값) 함수 : 변수 또는 값의 타입을 확인하는 내장 함수
# 정수 ( int ) Integer
n = 123
print(n, type(n))

price = 1_000_000_000; # 정수 자릿수 구분
print(price, type(price))

# 정수 ( int ) 최대걊
import sys
print(sys.maxsize)
print(type(sys.maxsize))

# 2진법, 8진법, 16진법
a = 0b100 #4
print(a, type(a))

b = 0o23 #19
print(b, type(b))

c = 0xff #255
print(c, type(c))

#------------------------------------------
# 실수(float)
f1 = 123.456
print(f1, type(f1))

f2 = -99999.99999 # 소숫점 아래 16자리까지 가능
print(f2, type(f2))

#------------------------------------------
# 복소수(complex)
c = 2j
print(c, type(c))

d = 3 + 4j
print(d, type(d))

#------------------------------------------
# 산술 연산 ( +, -, *, /, //(몫만구함), %(modulo, 나머지만구함), **(거듭제곱))
print("--산술연산--")
print(1 + 2) # 3
print(1 - 2) # -1
print(1 * 2) # 2
print(1 / 2) # 0.5 -> 나누어 떨어질 때까지의 몫
print(1 // 2) # 0 -> 정수 영역에서의 몫
print(1 % 2) # 1 -> 정수 영역에서의 나머지
print(3 ** 2) # 9 거듭제곱
print(2 ** 63) # int 양의 최대값



