# 산술 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8 : 거듭제곱
print(5%3) # 2 : 나머지 구하기
print(10%3) # 1
print(5//3) # 1 : 몫 구하기
print(10//3) # 3

# 비교 연산자
print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # 좌변과 우변이 똑같은가? => True
print(3+4 == 7) # True
print(1 != 3) # True
print(not(1 != 3)) # False

# 논리 연산자
print((3 > 0) and (3 < 5)) # True : AND 게이트
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 < 5)) # True : OR 게이트
print((3 > 0) | (3 > 5)) # True

print(not(3 == 3)) # False : NOT 게이트 => 값을 반전

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

# 할당 연산자
a = 1 # 우변의 값을 좌변으로 대입
b = 2
c = 3

c += b # 5 : c = c + b를 간추린 것
c -= b # 3 : c = c - b를 간추린 것
c *= b # 3 : c = c * b를 간추린 것
c /= b # 몰루 : c = c / b를 간추린 것
c %= b # 1 : c = c % b를 간추린 것
c **= b # 9 : c = c ** b를 간추린 것

# 숫자 처리 함수
print(abs(-5)) # 5 : 절댓값
print(pow(4, 2)) # 4^2 = 4*4 = 16 : 거듭제곱
print(max(5, 12)) # 12 : 입력받은 값들 중 가장 큰 값
print(min(5, 12)) # 5 : 입력받은 값들 중 가장 작은 값
print(round(3.14)) # 3 : 반올림
print(round(3.99)) # 4 : 반올림

from math import *
print(floor(4.99)) # 4 : 내림
print(ceil(3.14)) # 4 : 올림
print(sqrt(16)) # 4 : 제곱근
