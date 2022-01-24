# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_duplicate_id(target_username, username_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # 신규 생성한 이름이 기존 아이디 리스트에 있는지 확인하기 위해 연산자 in 사용
    # 아닐 경우 if 문을 자연스럽게 빠져나가게 되고, False 반환
    if target_username in username_list:
        return True
    return False
    

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    target_username = 'jungssafy'
    username_list = ['kimssafy', 'jungssafy']
    print(check_duplicate_id(target_username, username_list)) # True
