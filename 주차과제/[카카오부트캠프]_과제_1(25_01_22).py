# -*- coding: utf-8 -*-
"""[카카오부트캠프] 과제 1(25.01.22).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z_xAyy0EH5ndel3vEvPg4FQNoQJ7XuUH
"""

#전역 변수 설정
total_amount = 0
# name = '' # 사용자 이름 -> 인스턴스 변수로 변경(객체지향 프로그래밍에 맞게)
menu_bucket_list =[] #장바구니 리스트

class Menu: #메뉴판
    def menu_list_main() :
        menu_list_main = {
            '1. 치즈 햄버거 - 5000원':5000 ,
            '2. 불고기 햄버거 - 7000원':7000,
            '3. 쉬림프 햄버거 - 7000원':7000,
            '4. 빅 햄버거 - 8500원':8500
        }
        for i in menu_list_main:
            print(i) # 메인 메뉴판 공개

    def menu_list_side() :
        menu_list_side = {
            '1. 감자튀김 - 2500원':2500,
            '2. 해쉬 브라운 - 2500원':2500,
            '3. 너겟 - 3000원':3000
        }
        for i in menu_list_side:
            print(i) # 사이드 메뉴판 공개

    def menu_list_drink() :
        menu_list_drink = {
            '1. 콜라 - 2500원':2500,
            '2. 사이다 - 2500원':2500,
            '3. 환타 - 2500원':2500
        }
        for i in menu_list_drink:
            print(i) # 음료 메뉴판 공개

class Bucket: # 메뉴 장바구니
    @staticmethod #정적 메서드
    def menu_bucket_list_func(item) :
        global menu_bucket_list #갱신되는 리스트
        menu_bucket_list.append(item)

#사용자 입력
class User:
    def __init__(self):
        self.name = " " #인스턴스 변수 초기값 설정

    def user_info(self): #일반 메서드
        print("-------------------Welcome---------------------")
        while True :
            print("이름을 입력하십시오.")
            self.name = input() # 사용자 이름 입력
            print(self.name + "님이 맞습니까? Y/N")
            user_name_check = input()

            if user_name_check == 'Y' :
                print("----------------------------------------")
                print("안녕하세요" " "+ self.name + "님!")
                print("랜덤으로 지급액이 산정되며")
                print("해당 지급액으로 주문이 가능합니다!^^")

                pass # 추후 개발
                Order.start() # 주문 시작
                break
            elif user_name_check == 'N' :
                print("이름을 다시 입력하십시오.")
                continue
            else :
                print("잘못 입력하셨습니다.")
                continue

#주문
class Order:
    def start(): #주문 시작
        print("어서오세요:)")
        while True :
            print("주문을 하시겠습니까? Y/N")
            order_select = input()
            if order_select == 'Y' :
                print("주문을 시작합니다.")
                Order.pickOrder() # 주문 함수 호출
                break
            elif order_select == 'N' :
                print("주문을 취소합니다.")
                print("초기화면으로 돌아갑니다.")
                return #함수종료
            else :
                print("잘못 입력하셨습니다.")
                continue

    def pickOrder() : # 주문 함수
        global total_amount # 전역 변수 호출
        print("--------------------MENU(Main)--------------------")
        Menu.menu_list_main()
        while True :
            print("메인 메뉴 번호를 입력하십시오.")
            menu_list_main_select_number = int(input()) #메인 메뉴 선택

            if menu_list_main_select_number == 1 :
                total_amount += 5000 #총 결제 금액에 메뉴 가격 추가
                print("치즈 햄버거가 선택되었습니다.")
                Bucket.menu_bucket_list_func("치즈햄버거")
                print("주문품목 :" + ",".join(menu_bucket_list))
                print("총금액 : " + str(total_amount) + "원")
                Order.menu_list_side_function() #사이드 메뉴 함수 호출
                break
            elif menu_list_main_select_number == 2 :
                total_amount += 7000 #총 결제 금액에 메뉴 가격 추가
                print("불고기 햄버거가 선택되었습니다.")
                Bucket.menu_bucket_list_func("불고기햄버거")
                print("주문품목 :" + ",".join(menu_bucket_list))
                print("총금액 : " + str(total_amount) + "원")
                Order.menu_list_side_function() #사이드 메뉴 함수 호출
                break
            elif menu_list_main_select_number == 3 :
                total_amount += 7000 #총 결제 금액에 메뉴 가격 추가
                print("쉬림프 햄버거가 선택되었습니다.")
                Bucket.menu_bucket_list_func("쉬림프햄버거")
                print("주문품목 :" + ",".join(menu_bucket_list))
                print("총금액 : " + str(total_amount) + "원")
                Order.menu_list_side_function() #사이드 메뉴 함수 호출
                break
            elif menu_list_main_select_number == 4 :
                total_amount += 8500 #총 결제 금액에 메뉴 가격 추가
                print("빅 햄버거가 선택되었습니다.")
                Bucket.menu_bucket_list_func("햄버거")
                print("주문품목 :" + ",".join(menu_bucket_list))
                print("총금액 : " +str(total_amount) + "원")
                Order.menu_list_side_function() #사이드 메뉴 함수 호출
                break
            else :
                print("메뉴판에 없는 메뉴입니다.")
                continue

    def menu_list_side_function() : #사이드 주문 여부 확인
        global total_amount # 전역 변수 호출(값이 수정되므로 global 키워드 사용)
        print("----------------------------------------")
        while True :
            print("사이드 메뉴를 선택하시겠습니까? Y/N")
            menu_list_side_select = input()
            if menu_list_side_select == 'Y' :
                print("사이드 메뉴판 입니다.")
                print("--------------------MENU(Side)--------------------")
                Menu.menu_list_side()
                while True :
                    print("사이드메뉴 번호를 선택하십시오.")
                    menu_list_side_number = int(input())
                    if menu_list_side_number == 1 :
                        total_amount += 2500 #총 결제 금액에 메뉴 가격 추가
                        print("감자튀김이 선택되었습니다.")
                        Bucket.menu_bucket_list_func("감자튀김")
                        print("주문품목 :" + ",".join(menu_bucket_list))
                        print("총금액 : " +str(total_amount) + "원")
                        Order.menu_list_drink_function()
                        break
                    elif menu_list_side_number == 2 :
                        total_amount += 2500 #총 결제 금액에 메뉴 가격 추가
                        print("해쉬 브라운이 선택되었습니다.")
                        Bucket.menu_bucket_list_func("해쉬브라운")
                        print("주문품목 :" + ",".join(menu_bucket_list))
                        print("총금액 : " + str(total_amount) + "원")
                        Order.menu_list_drink_function()
                        break
                    elif menu_list_side_number == 3 :
                        total_amount += 3000 #총 결제 금액에 메뉴 가격 추가
                        print("너겟이 선택되었습니다.")
                        Bucket.menu_bucket_list_func("너겟")
                        print("주문품목 :" + ",".join(menu_bucket_list))
                        print("총금액 : " + str(total_amount) + "원")
                        Order.menu_list_drink_function()
                        break
                    else :
                        print("잘못 입력하셨습니다.")
                        continue
            elif menu_list_side_select == 'N' :
                print("사이드 메뉴를 선택하지 않으셨습니다.")
                Order.menu_list_drink_function() #음료 함수로 호출
                break
            else :
                print("잘못 입력하셨습니다.")
                continue

    def menu_list_drink_function(): #음료 주문 여부 확인
        global total_amount # 전역 변수 호출(값이 수정되므로 global 키워드 사용)
        print("----------------------------------------")
        while True :
            print("음료를 선택하시겠습니까? Y/N")
            menu_list_drink_select = input()
            if menu_list_drink_select == 'Y' : # 예 선택
                print("음료 메뉴판 입니다.")
                print("--------------------MENU(Drink)--------------------")
                Menu.menu_list_drink()
                while True :
                    print("음료를 선택하십시오.")
                    menu_list_drink_number = int(input())
                    if menu_list_drink_number == 1 :
                        total_amount += 2500 #총 결제 금액에 메뉴 가격 추가
                        print("콜라가 선택되었습니다.")
                        Bucket.menu_bucket_list_func('콜라')
                        print("주문품목 :" +",".join(menu_bucket_list))
                        print("총금액 : " +str(total_amount) + "원")
                        Pay.pay() #결제 함수 호출
                        break
                    elif menu_list_drink_number == 2 :
                        total_amount += 2500 #총 결제 금액에 메뉴 가격 추가
                        print("사이다가 선택되었습니다.")
                        Bucket.menu_bucket_list_func('사이다')
                        print("주문품목 :" +",".join(menu_bucket_list))
                        print("총금액 : " +str(total_amount) + "원")
                        Pay.pay() #결제 함수 호출
                        break
                    elif menu_list_drink_number == 3 :
                        total_amount += 2500 #총 결제 금액에 메뉴 가격 추가
                        print("환타가 선택되었습니다.")
                        Bucket.menu_bucket_list_func('환타')
                        print("주문품목 :" +",".join(menu_bucket_list))
                        print("총금액 : " +str(total_amount) + "원")
                        Pay.pay() #결제 함수 호출
                        break
                    else :
                        print("잘못 입력하셨습니다.")
                        continue
            elif menu_list_drink_select == 'N' : # 아니오 선택
                print("음료를 선택하지 않으셨습니다.")
                Pay.pay() #결제 함수 호출
                break
            else :
                print("잘못 입력하셨습니다.")
                continue
#결제
class Pay:
    def pay(): #결제 모듈
        global total_amount # 전역 변수 호출(값이 수정되므로 global 키워드 사용)
        global menu_bucket_list # 전역 변수 호출(값이 수정되므로 global 키워드 사용)
        print("--------------------PAY--------------------")
        print("총 주문 금액은" + str(total_amount)+ "원 이며")
        print("주문하시는 품목은" + str(menu_bucket_list) + "입니다.")
        while True :
            print("결제를 하시겠습니까? Y/N")
            pay_select = input()
            if pay_select == 'Y' : # 예 선택
                print("결제를 시작합니다.")
                print("결제 방식을 입력해주십시오.")
                print("cash or card")
                while True :
                    pay_method = input()
                    if pay_method == 'cash' :
                        PayCash.pay_method_Cash() # 현금 결제 함수 호출
                        break
                    elif pay_method == 'card' :
                        PayCard.pay_method_Card() # 카드 결제 함수 호출
                        break
                    else :
                        print("잘못 입력하셨습니다.")
                        continue
            elif pay_select == 'N' :
                print("결제를 취소하시겠습니까?")
                print("현재 저장된 데이터는 사라집니다 Y/N")
                while True :
                    pay_select_cancle = input()
                    if pay_select_cancle == 'N' :
                        return Pay.pay()
                        break
                    elif pay_select_cancle == 'Y' :
                        print("초기 화면으로 돌아갑니다.")
                        return Order.start()
                        break
                    else :
                        print("잘못 입력하셨습니다.")
                        continue
            else :
                print("잘못 입력하셨습니다.")
                continue

#현금결제
class PayCash:
    def pay_method_Cash():
        global total_amount # 전역 변수 호출(값이 수정되므로 global 키워드 사용)
        while True:
            print("현금 결제를 시작합니다.")
            print("--------------------PAY(Cash)--------------------")
            print("총 결제 금액은" + str(total_amount) + "원 입니다.")
            print("투입할 금액을 입력해주십시오.")
            try :
                total_amount_input = int(input()) # 현금 금액 입력
            except :
                print("잘못 입력하셨습니다.")
                continue

            #금액이 부족한 경우
            while total_amount_input < total_amount:
                print("금액이 부족합니다.")
                print("필요한 금액 :" + str(total_amount - total_amount_input) + "원")
                print("금액을 더 입력해주십시오.")
                try:
                    amount_input = int(input()) #추가 금액 입력
                    total_amount_input += amount_input
                except ValueError:
                    print("잘못 입력하셨습니다.")
                    continue

            #결제가 완료된 경우
            print("잔돈은 " + str(total_amount_input - total_amount) + "원 입니다.")
            print("결제가 완료되었습니다.")
            print("현금 영수증을 출력하시겠습니까? Y/N")
            while True :
                if input() == 'Y' :
                    Receipt.receipt_cash() #현금영수증 함수 호출
                    break
                elif input() == 'N' :
                    print("결제가 완료되었습니다. 감사합니다.")
                    return
                else :
                    print("잘못 입력하셨습니다.")
                    continue
           
#카드결제
class PayCard:
    def pay_method_Card():
        global total_amount # 전역 변수 호출(값이 수정되므로 global 키워드 사용)
        print("카드 결제를 시작합니다.")
        print("--------------------PAY(Card)--------------------")
        print("총 결제 금액은 " + str(total_amount) + "원 입니다.")
        print("카드 결제중입니다...")
        print("결제가 완료되었습니다.")
        Receipt.receipt_card() #영수증 함수 호출
        # else :
        #     print("잘못 입력하셨습니다.")
        #     while True :
        #         pay_select = input("다시 결제 하시겠습니까? Y/N")
        #         if pay_select == 'Y':
        #             return Pay.pay()
        #         elif pay_select == 'N' :
        #             print("--------------------WARNNING--------------------")
        #             print("결제를 취소하시겠습니까? 초기로 돌아갑니다. Y/N ")
        #             pay_select_cancle = input()
        #             if pay_select_cancle == 'Y' :
        #                 return Order.start() #초기로 return
        #             elif pay_select_cancle == 'N' :
        #                 return PayCard.pay_method_Card() #결제
        #                 break
        #         else :
        #             print("잘못 입력하셨습니다.")
        #             continue
#영수증
class Receipt:
    def receipt_card():
        global total_amount # 전역 변수 호출
        print("영수증을 출력하시겠습니까? Y/N")
        receipt_respon = input()
        while True :
            if receipt_respon == 'Y':
                print("영수증 출력이 되었습니다.")
                print("최종 금액은" + str(total_amount) + "원 입니다.")
                print("감사합니다.")
                break
            elif receipt_respon == 'N':
                print("영수증을 출력하지 않습니다.")
                print("결제가 완료되었습니다. 감사합니다.")
                break #종료
            else :
                print("잘못 입력하셨습니다.")
                continue
    def receipt_cash():
        global total_amount # 전역 변수 호출
        print("현금영수증을 출력하시겠습니까? Y/N")
        while True:
            receipt_cash_respon = input()
            if receipt_cash_respon == 'Y':
                print("영수증 번호를 입력해주세요.")
                receipt_cash_number = int(input())
                print(str(receipt_cash_number) + "입력 되었습니다.")
                print("현금 영수증이 출력되었습니다.")
                print("최종 금액은" + str(total_amount) + "원 입니다.")
                print("감사합니다.")
                break
            elif receipt_cash_respon == 'N':
                print("현금영수증을 출력하지 않습니다.")
                print("결제가 완료되었습니다. 감사합니다.")
                break #종료
            else :
                print("잘못 입력하셨습니다.")
                continue
#프로그램 시작
user = User()
user.user_info() # 사용자 입력 메서드 실행

