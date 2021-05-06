list_number = [52, 273, 32, 72, 100]
while True:
    try :
        number = int(input("정수입력"))
        print(list_number.index(number))

    except ValueError :
        print("정수만을 압력하세요.")
    except IndexError :
        print("인덱스에 주의해주세요.")
    except Exception :
        print("예기치 못한 문제가 발생했습니다..")