'''
    세개의 정수를 인자로 받아,
    합계와 평균을 출력해주는 함수를 만드시오.

    예) 합계: 평균:
'''

def sum(a, b, c):
    return a+b+c


def ave(a, b, c):
    return (a+b+c)/3

print("합계 :", sum(1,2,3), "평균 :", ave(1,2,3))

# 설명문 (docstring) """ """
# 문자열 포매팅(f"")
def pirnt_sum_avg(a,b,c):
    """
    세개의 숫자를 받아 합계와 평균을 출력하는 함수
    :param a:
    :param b:
    :param c:
    :return:
    """

    sum = c + b + a
    avg = sum / 3

    print(f"합계: {sum} 평균: {avg} ")

pirnt_sum_avg(10, 20, 30)
pirnt_sum_avg(30, 40, 50)
