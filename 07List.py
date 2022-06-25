# 리스트 []

# 지하철 칸 별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["사람1", "사람2", "사람3"]
print(subway)

# 사람2가 몇 번째 칸에 타고 있는가?
print(subway.index("사람2"))

# 사람4가 다음 정류장에서 다음 칸에 탐
subway.append("사람4")
print(subway)

# 사람5를 사람1 / 사람2 사이에 태우기
subway.insert(1, "사람5") # 1번째 자리에 집어넣고 뒤에 있던 것들은 뒤로 밀림
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("사람1")
print(subway)
print(subway.count("사람1"))

# 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["사람1", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)