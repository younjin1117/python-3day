a = "Hello world"
print(type(a))

# \는 문자열로 쓰겠다는 의미
# \n는 문자열 안에서 줄을 바꿀때 사용
# \t는 탭만큼 간격을 줄 때 사용
# """이거는 그냥 엔터만써도 자동 줄바꿈된당
a="life is too short\000you need python"
print(a)
a="""
life is too short
you need python
ah hagi silta
"""
print(a)

a = "python"
b = "is fun!"
print(a*100)
print(a+b)

#예제 'you need python'문장을 문자열로 만들고 길이를 구해보자
a="you need python"
print("문자열길이",len(a))

# 문자열 인덱싱과 슬라이싱 
a= "life is too short, you need python"
print(a[0])

# 문자열 포매팅
number = 10
day = "three"
a = "i ate %d apples. so i was sick for %s day."%(number,day)

print(a)

# .find는 그거 갯수 찾아줌
a = "hobby"
print(a.find('b'))

# join하면 사이에 "" 사이에거 다 박아줌
a = ",".join("abcd")

print(a)

# .upper는 대문자로 만들기 .lower는 소문자로 만들기
a = "hi"

print(a.upper())

# replace 는 바꾸깅
a = "life is too short"
print(a.replace("life","leg"))

# split는 문자열이 있으면 띄어쓰기 기준으로 리스트로 만듬
a = "life is too short" 
print(a.split())

# list  append 원소를 리스트에추가 리스트도 가능
# sort 알파벳이나 숫자를 순서대로 정렬해주는것
# reverse 리스트 순서를 정반대로 하는것
# index 갯수 찾기
# insert 특정위치에 특정원소 넣기
# remove 특정위치에 리스트 지우기
# pop 특정위치에 리스트 꺼내기
# extend 특정리스트를 리스트에 추가

a = [1,2,3]
a.append(4)
print(a)

a = [1,4,2,3]
a.sort()
print(a)

a = [1,2,3,4]
a.reverse()
print(a)

a = [1,2,3,4]
print(a.index(2))

a = [1,2,3,4]
a.insert(1,1.5)
print(a)

a = [1,2,3,4]
a.remove(1)
print(a)

a = [1,2,3,4]
a.pop()
print(a)

a = [1,2,3,4]
a.extend([2.5,3.5])
print(a)