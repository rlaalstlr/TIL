# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # 시저 암호를 반환하기 위해 빈 문자열 생성
    new_word = ''

    # word를 순회하며 한 글자씩 변환
    for alphabet in word:
        # string 내부의 각 char들을 아스키 코드로 변환
        # 그 후 n 만큼 밀기
        ascii_num = ord(alphabet)

        # 소문자일 경우
        if ascii_num in range(97,123):
            ascii_num += n
            # ascii 테이블 범위를 벗어났을 경우의 예외처리, 다시 26만큼 앞으로 당깁니다.
            if ascii_num not in range(97, 123):
                ascii_num -= 26

        # 대문자일 경우
        if ascii_num in range(65, 91):
            ascii_num += n
            # ascii 테이블 범위를 벗어났을 경우의 예외처리, 다시 26만큼 앞으로 당깁니다.
            if ascii_num not in range(65, 91):
                ascii_num -= 26

        # 마지막으로 아스키 코드에서 다시 char형으로 변환
        new_alphabet = chr(ascii_num)
        new_word += new_alphabet

    return new_word


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx