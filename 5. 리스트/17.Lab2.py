'''
    턱걸이 평균 측정 프로그램을 만들어 보시오.
    먼저, 턱걸이 횟수를 저장할 빈 리스트를 만드시오.
    그리고 일주일간의 턱걸이 횟수를 입력 받아서 리스트에 저장하시오.
    리스트에 저장된 데이터의 평균을 구해 출력하시오.

    예시)
        1일차 턱걸이 홋수 >>>
        2일차
        3일차
        4일차
        5일차
        6일차
        7일차

        22
'''

턱걸이1 = int(input("1일차:"))
턱걸이2 = int(input("2일차:"))
턱걸이3 = int(input("3일차:"))
턱걸이4 = int(input("4일차:"))
턱걸이5 = int(input("5일차:"))
턱걸이6 = int(input("6일차:"))
턱걸이7 = int(input("7일차:"))

턱걸이리스트 = [턱걸이1, 턱걸이2, 턱걸이3, 턱걸이4, 턱걸이5, 턱걸이6, 턱걸이7]

턱걸이총합 = 턱걸이1 + 턱걸이2 + 턱걸이3 + 턱걸이4 + 턱걸이5 + 턱걸이6 + 턱걸이7

턱걸이평균 = 턱걸이총합 / 7
print("턱걸이리스트 =", 턱걸이리스트)
print("턱걸이총합 = ", 턱걸이총합)
print("턱걸이평균 = ", 턱걸이평균)


# 리스트 추가
data = []


x = int(input("1일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("2일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("3일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("4일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("5일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("6일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("7일차 턱걸이 횟수 >>>"))
data.append(x)




total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]
avg = total / 7

print("턱걸이 평균 횟수 >>>", int(avg))