# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # 계산의 편의를 위해 position을 x와 y 좌표로 분리
    (x, y) = position

    # M의 값에 따른 좌표값 변화
    if M == 0:
        (x, y) = (x - 1, y)
    elif M == 1:
        (x, y) = (x + 1, y)
    elif M == 2:
        (x, y) = (x, y - 1)
    elif M == 3:
        (x, y) = (x, y + 1)
    
    # x 와 y 좌표가 둘 다 범위 내에 있을 경우에만 참, 나머지 거짓
    if x in range(0, N) and y in range(0, N):
        return True
    else:
        return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0))) # True
    print(is_position_safe(3, 0, (0, 0))) # False
