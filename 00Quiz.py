
#1.Quiz) 변수를 이용하여 다음 문장을 출력하시오

#변수명 : station
#변수값 : "사당", "신도림", "인천공항" 순서대로 입력
#출력 문장 : XX행 열차가 들어오고 있습니다.

station = ["사당", "신도림", "인천공항"]

for i in range(1, 4):
    print(*station[i-1:i], "행 열차가 들어오고 있습니다.")

"""
2.Quiz) 당신은 최근에 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 X일로 선정되었습니다."""

from random import *

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 ", str(date), "일로 선정되었습니다.")

"""
3.Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) https://naver.com
규칙1 : https:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
                (nav)               (5)             (1)         (!)
예) 생성된 비밀번호 : nav51!
"""

url = "https://github.com/"
result = url.replace("https://", "") # 규칙1
result = result[:result.find(".")] # result[0:5]
password = result[:3] + str(len(result)) + str(result.count("e")) + "!"
print("{0} 사이트의 비밀번호는 {1}입니다.".format(url, password))