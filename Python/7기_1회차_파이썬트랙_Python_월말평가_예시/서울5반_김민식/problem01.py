# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def total(scores):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    total_score = 0 # 반환할 값을 0으로 초기화
    # scores 리스트를 순회하기 위한 for문
    for score in scores:
        total_score += score
    # score의 값을 전부 total_score에 합산해서 반환
    return total_score


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(total(scores)) # 330
