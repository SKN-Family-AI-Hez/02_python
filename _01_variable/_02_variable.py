# 변수 (variable)
# - 값(literal)을 저장하는 메모리 상의 공간
# - 각 변수바다 이름이 지정되어 있음 (이름을 불러서 사용)

# 변수 선언 방법
# 변수명 = 값
a = 10 # a 라는 메모리 상의 공간에 10 (literal)을 대입
b = "홍길동"
print("a =", a)
print("b =", b)

# 대입 연산자(=)
# - 우항의 값을 좌항의 변수에 대입 (무조건 우항에서 좌항으로 대입)
num = 100
print("num =", num)

# 변수는 저장된 값이 계속 변할 수 있다.
num = 999
print("num =", num)

num = "abcdefg"
print("num =", num)

# 변수 명명 규칙
# 1. 의미 있는 이름 사용
# 2. 변수명은 snake case 를 사용 ( 소문자 + _ )
# 단, 대문자도 사용은 가능하나 소문자와 구분된다 ( A != a )
team_name = "오지라퍼스"
Team_name = "Ohgiraffers"
print(team_name)    # 오지라퍼스
print(Team_name)    # Ohgiraffers

# 한글 가능
밥조 = "3조"
print("밥조: ", 밥조)

# 변수명은 숫자로 시작해서는 안 된다.(문법 오류 발생)
name_1 = "콩쥐"
# 1_name = "팥쥐" -> X 문법 에러
_1_name = "신데렐라" # 숫자를 앞에 두어야 하는 경우 "_" 사용

# 특수 문자는 언더스코어를 제외하고 사용 불가
# team-name -> X
# team@name -> X

# 예약어는 변수명으로 사용 불가 ex. if, for, while, else, elif, etc.

# 파이썬 예약어 종류 확인
import keyword
print(keyword.kwlist)