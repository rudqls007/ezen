# 비만도 계산기를 만들어 보시오


'''

예시 )
        BMi 계산기 입니다.
        신장:
        몸무게:
        BMI:

'''

print("BMI 계산기 입니다.")
cm = int(input("신장: >>>"))
kg = int(input("몸무게: >>>"))
result = kg / (cm * cm) * 10000
print(result)


print("BMI 계산기 입니다.")
cm = input("신장: ")
kg = input("몸무게: ")
cm = int(cm)
kg = int(kg)

BMI = kg / (cm * cm) * 10000
print(BMI)