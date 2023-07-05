# # 문자열
# sentance = '나는 소년입니다'
# print(sentance)
# sentance2 = "파이썬은 쉬워요"
# print(sentance2)
# sentance3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentance3)

# ----------------------------------------------------------------------------------------------------

# # 슬라이싱
# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 1~2번째 값을 출력
# print("월 : " + jumin[2:4]) # 3~4번째 값을 출력
# print("일 : " + jumin[4:6]) # 5~6번째 값을 출력
# print("생년원일 : " + jumin[:6]) # 처음부터 6번째 값을 출력
# print("뒤 7자리 : " + jumin[7:]) # 8부터 끝까지 값을 출력
# print("뒤 7자리(뒤에서 부터) : " + jumin[-7:]) #맨 뒤에서 7번재붜 끝까지

# ----------------------------------------------------------------------------------------------------

# # 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("n"))
# print(python.find("Java"))
# # print(python.index("Java")) #문자(Java))가 없어서 오류

# print(python.count("n"))

# ----------------------------------------------------------------------------------------------------

# #문자열 포맷

# # 방법 1
# print("나는 %d살입니다." % 20) # d는 정수 값을 의미함.
# print("나는 %s을 좋아해요." % "파이썬") # s는 문자열를 의미함.
# print("Aplle은 %c로 시작해요." % "A") # c는 문자를 의미함.
# # %s는 정수랑 문자랑 상관없이 출력 가능
# print("나는 %s살입니다." % 20) 
# print("나는 %s을 좋아해요." % "파이썬")
# print("Aplle은 %s로 시작해요." % "A") 

# print("나는 %s색과 %s색을 좋아해요." %("파란", "빨강"))

# #방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨강"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨강"))

# #방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# # 방법 4(V3.6 이상)
# age = 20
# color = "삘긴"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# ----------------------------------------------------------------------------------------------------

# # 탈출 문자
# print("백문이 물여일견 \n 백견이 불여일타") # \n : 줄바꿈

# # 출력문 : 저는 "나도 코딩"입니다.
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.") #\", \' : 문잔내에서 따옴표
# print('저는 \'나도코딩\'입니다.')

# \\ : 문장 내에서 \
# print("cd \\Users\\bagsangmin\\Desktop\\For-my-study-Python")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# #  \b : 백스페이스(한 글자 삭제)
# print("Redd\bApple")

# # \t :  탭 기능
# print("Red\tApple")

# ----------------------------------------------------------------------------------------------------

#Quiz) 사이트별로 비밀번로를 만들어주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1 : http://부분은 제외 => naver.compile
# 규칙2 : 처음 만나는 점(.) 이후 무분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 예) 네이버에 생성된 비밀번호 : nav51!

url = "http://naver.com"
site1 = url.replace("http://", "") # 규칙 1
# print(site)
site2 = site1[:site1.index(".")] # 규칙 2
# print(site2)
pw = site2[:3] + str(len(site2)) + str(site2.count("e")) + "!"
print("{0}에 생성된 {1} : ".format("네이버", "비밀번호") + pw)