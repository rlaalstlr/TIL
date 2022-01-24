# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def get_final_position(N, mat, moves):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.


    # 현재 위치를 [x, y]라고 한다.
    [x, y] = [0, 0]

    # 주어진 2차원 리스트를 순회하며 현재 위치 좌표를 찾는다.
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            # 현재 위치가 1로 표시되고, 나머지는 전부 0 이므로
            if mat[i][j]:
                [x, y] = [i, j]

    # moves 리스트 내의 모든 움직임 입력받기
    for M in moves:
        # M의 값에 따른 좌표값 변화
        if M == 0:
            [x, y] = [x - 1, y]
        elif M == 1:
            [x, y] = [x + 1, y]
        elif M == 2:
            [x, y] = [x, y - 1]
        elif M == 3:
            [x, y] = [x, y + 1]
    
    # x 와 y 좌표가 둘 다 범위 내에 있을 경우에만 위치 반환, 아니라면 None 반환
    if x in range(0, N) and y in range(0, N):
        return [x, y]
    else:
        return None


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    N = 3
    mat = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ] 
    moves1 = [1, 1, 3]
    print(get_final_position(N, mat, moves1)) # [2, 1]
    
    moves2 = [1, 3, 3]
    print(get_final_position(N, mat, moves2)) # [1, 2]