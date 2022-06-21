# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "카멜"입니다.

 # 방법 1
print("저는 '카멜'입니다.")
print('저는 "카멜"입니다.')

# 방법 2
print("저는 \"카멜\"입니다.")
print("저는 \'카멜\'입니다.")

# \\ : 문장 내에서 \
print("C:\\Users")

# print("C:\Users") : 에러
# print("C:\\Users") : 정상 작동

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # 커서를 맨 앞으로 이동 후 원래 문자열에 덮어쓰기

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")