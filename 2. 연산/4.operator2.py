# 비교연산
print(2 > 3)    #false
print(15 < 30)  #true
print(1.5 >= 0) #true
print(3 <= 3)   #true
print("주변음" == "주변옴")   #false
print("11111111111" == "11111111111") #true

print(" ")

# 논리연산
print(4 < 6 and 10 >= 10) #true and true => true
print("적용형 주변음 허용 모드" != "적용형 주변음 허용 모드" or "나는 할 수 있다" == "나는 할 수 있다") #false or true => true
print(not 5 == 5)   #not true => false

print(" ")

# 맴버십 연산자
# in - 포함되어 있다
# not in - 포함되어 있지 않다
print("a" in "abc") # true
print("d" not in "abc") # true
