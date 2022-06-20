# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고, 파이썬은 쉬워요
"""
print(sentence3)

#슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7]) # 파이썬에서 문자를 셀 땐 0부터 시작
print("연 : " + jumin[0:2]) # 0번째부터 2번째 직전까지 (0, 1)
print("월 : " + jumin[2:4]) # 2번째부터 4번째 직전까지 (2, 3)
print("일 : " + jumin[4:6]) # 4번째부터 6번째 직전까지 (4, 5)

print("생년월일 : " + jumin[:6]) # 처음부터 6번째 직전까지 (0, 1, 2, 3, 4, 5)
print("뒤 7자리 : " + jumin[7:]) # 7번째부터 끝까지 (7, 8, 9, 10, 11, 12, 13)
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 모든 문자 소문자 처리
print(python.upper()) # 모든 문자 대문자 처리
print(python[0].isupper()) # 특정 문자가 대문자인지 검사 후 bool 형으로 출력
print(len(python)) # 문자열의 길이
print(python.replace("Python", "Java")) # Python 문자열을 Java로 변환

index = python.index("n") # n이란 문자가 어느 위치에 있는지 검사
print(index)
index = python.index("n", index + 1) # n을 찾되, 위 코드에서 찾은 n의 위치 다음 문자부터 검사
print(index)

print(python.find("Java")) # n이란 문자가 어느 위치에 있는지 검사, 없으면 -1 출력
print(python.index("Java")) # 찾는 문자가 없으면 오류 발생

print(python.count("n")) # n이란 문자가 몇 개 있는지 검사