# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) # Double 형
print("나는 %s을 좋아해요." % "파이썬") # String 형
print("Apple은 %c로 시작해요." % "A") # Char 형

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 여러 개 추가

# 방법 2
print("나는 {}살입니다.".format(20)) # 위 코드와 같은 것
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # 여러 개 추가
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 중괄호 안에 숫자로 순서를 정할 수 있음
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간")) # 변수로 활용 가능
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))
# 변수의 순서를 바꿔도 결과는 똑같다.

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
# 외부 변수도 활용 가능 단, f를 붙여야함 넣지 않으면 그냥 문자열로 출력됨

# print(f"나는 {age}살이며, {color}색을 좋아해요.") : O
# print("나는 {age}살이며, {color}색을 좋아해요.") : X