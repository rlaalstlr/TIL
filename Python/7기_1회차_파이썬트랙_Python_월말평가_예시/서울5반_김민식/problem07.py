# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def dec_to_bin(n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # 이진수 숫자를 차례로 담을 빈 문자열 생성
    bin_str = ''
    # 반복조건: n 이 1 보다 클 때
    if n > 1:
        # 2로 나눈 나머지를 문자열 맨 끝에 추가하고, 몫은 다시 dec_to_bin 함수에 넣어준다
        bin_str = dec_to_bin(n // 2) + str(n % 2)
        return bin_str
    else:
        # 반환값이 str형 이어야 하므로 예외없이 str()함수로 처리
        return str(n % 2)



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # 1010
    print(dec_to_bin(5))
    # 101
    print(dec_to_bin(50))
    # 110010