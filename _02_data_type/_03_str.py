# str (문자형, 문자열, String)
# "", '', """ """, ''' ''' 감싸서 표현
print("---홑 따옴표, 쌍 따옴표---")
s1 = 'Hello'
s2 = "World"
print(s1, type(s1))
print(s2, type(s2))
s3 = "'abc'"
print(s3, type(s3)) # 홑따옴표가 문자 자체로 인식됨

# 삼중 다옴표
print('-------------')
print("""
삼중따옴표는
입력된 형식 그대로 문자열(str)로 변환
""")
print('-------------')
print("""앞/뒤 엔터 없이 작성하려면
따옴표와 문자열을 딱 붙여서 작성""")
print('-------------')

# str 연산
# 1. 문자열 + 문자열 = 이어쓰기
print('---문자열 더하기 연산---')
a = 'apple'
b = 'banana'
print(a + ', ' + b) # apple, banana

# 2. 문자열 * 양의 정수 = 양의 정수 크기 만큼 반복
print('-' * 30)

# 빼기, 나누기 연산은 불가

# len(객체)함수: 파이썬 객체 길이 반환
# 파이썬 객체: str, list, tuple, dict, set, etc.
print('---len()---')
text = '오늘 점심 뭐먹지'
print(text, len(text))

# ---str 메서드 (str API)---
# ( 참고 ) 함수, 메서드 == 기능( 실행 후 결과 반환 )

# str.replace(old, new)
# - str내에서 old에 해당하는 문자를 new로 치환(변경)
print('---str.replace()---')
today = '2026-06-01'
print(today, today.replace('-', '/'))

# str.strip([str])
# - 문자열 좌우 [str] 제거
# - [str]생략 시 공백 제거
# - 코드 작성법에서 []는 생략 가능을 의미
print('---str.strip()---')
some = '        하하하       '
print('[' + some + ']')
print('[' + some.strip() + ']')

# 대소문자 관련 str 메서드
print('--- 대소문자 관련 str메서드 ---')
origin_str = 'hELLO wORLD!'
print(origin_str.upper())         # HELLO WORLD!
print(origin_str.lower())         # hello world!
print(origin_str.capitalize())    # Hello world!
print(origin_str.swapcase())      # Hello World!
print(origin_str.title())         # Hello World!

# 문자열 포맷팅
# 1. % 포맷팅
print('---% 포맷팅---')
x = 10
print("x is %d" %x)    # x is 10

y = "code"
print("y is %s" % y)    # y is code


# 2. str.format()
print('---str.format()---')
x = 10
y = 1.23
print('{} + {} = {}'.format(x, y, x + y))
print("x is {0}".format(x))                                        # x is 10
print("x is {0} y is {1}".format(x,y))                             # x is 10 y is code
print("x is {new_x} and y is {new_y}".format(new_x=x, new_y=y))    # x is 10 and y is code

# 3. f-string ( python3.6, format string)
print('--- f-string ---')
print(f'{x} + {y} = {x+y}')

