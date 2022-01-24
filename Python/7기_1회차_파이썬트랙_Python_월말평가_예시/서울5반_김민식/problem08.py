# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def inventory_filter(item_type, inventory):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 딕셔너리를 담을 빈 리스트 생성
    item_list = []

    # inventory를 순회하는 for문
    for item in inventory:
        # 딕셔너리 내부의 type 키의 value 에 접근해서, 찾고자 하는 item_type과 같은지 비교
        if item_type == item.get('type'):
            # 리스트에 딕셔너리 추가
            item_list.append(item)

    return item_list


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    item_type = 'weapon'
    inventory = [
        {
            'id': 1,
            'name': 'Elder Wand',
            'type': 'weapon',
            'grade': 'legend',
        },
        {
            'id': 2,
            'name': 'Healing Potion',
            'type': 'potion',
            'grade': 'normal',
        },
        {
            'id': 3,
            'name': 'Steel Helmet',
            'type': 'armor',
            'grade': 'rare',
        },
        {
            'id': 4,
            'name': 'Long Sword',
            'type': 'weapon',
            'grade': 'normal',
        },
    ]
    print(inventory_filter(item_type, inventory)) 
    # [{'id': 1, 'name': 'Elder Wand', 'type': 'weapon', 'grade': 'legend'}, {'id': 4, 'name': 'Long Sword', 'type': 'weapon', 'grade': 'normal'}]
