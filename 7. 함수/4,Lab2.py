'''
    로또 예상번호 추출 프로그램을 구현하려고 합니다.
    다음 조건에 따라서 프로그램을 완성해 보시오.
        1) 로또 번호를 6개를 생성한다
        2) 로또 번호는 1~45까지의 랜덤한 번호다
        3) 6개의 숫자 모두 달라야 한다
        4) getRandomNumber() 함수를 사용해서 구현한다

        출력 예) 1 8 11 13 26 42

        - 리스트, 반복문, 조건문
'''
import random

def getRandomNumber():
    number = random.randint(1, 45)
    return number

# 로또 번호를 저장할 리스트
lotto_num = []
# 현재 뽑은 숫자 개수
count = 0

# for i in range(1,46):
#     rotto.append(i)
# print(rotto)

while True:
    if count > 5:
        break
    random_number = getRandomNumber()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1

lotto_num.sort()

for num in lotto_num:
    print(num, end=" ")



