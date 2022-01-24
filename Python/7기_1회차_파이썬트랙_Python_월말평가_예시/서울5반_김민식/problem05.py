# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_password_length(password):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # 비교 연산자를 사용하는 대신 깔끔한 range형 사용
    # password 문자열의 길이가 8이상, 33 미만이면 True 반환
    if len(password) in range(8, 33):
        return True

    return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    password = 'q1w2e3r4'
    print(check_password_length(password)) # True
