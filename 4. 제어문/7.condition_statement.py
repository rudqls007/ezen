# 제어문 - 조건문, 반복문
# ex)   기존 비밀번호 = "0111"
#       입력한 비밀번호 = "0111"
#       만약 비밀번호를 정확히 입력했으면 -> 로그인 성공
#       만약 입력을 안 했으면 -> 아무 것도 입력하지 않았습니다.

origin_pass = "0111"
input_pass = input("패스워드를 입력하시오 >>>")

if input_pass == origin_pass:       # 조건 A
    # 조건 A 참                                        if 문은 참인 경우에 들여쓰기가 된다. 들여쓰기가 끝나면 if 문과 무관하다.
    print("로그인 성공")
    print("환영합니다.")
elif input_pass == "":              # 조건 B
    # 조건 A 거짓, 조건 B 참
    print("아무 것도 입력하지 않았습니다.")
else:
    # 조건 A, B 모두 거짓
    print("로그인 실패")
    print("비밀번호를 확인하세요.")

