import random # 랜덤 모듈

def title(): # 로그인 타이틀
    print("--------------------------------------------------------------------------------")
    print("\t\t\t   < 주식 시뮬레이션 게임 >\n")
    
    print("1. 회원가입")
    print("2. 로그인")
    print("3. 게임 종료\n")

def sign_up(): # 회원가입 함수
    while True: # 아이디와 비밀번호의 조건이 맞을 때까지 반복
        print("\n아이디 5자 이상(영문 또는 숫자들로만 구성)")
        print("비밀번호 5자 이상(특수기호 최소 한 개)\n")
        
        id_c = input("아이디 입력: ")
        pwd_c = input("비밀번호 입력 : ")

        if ((len(id_c) < 5) or (id_c.isalnum() == False) or (len(pwd_c) < 5) or (pwd_c.isalnum() == True)):
            continue

        pwd_ck = input("비밀번호 확인 : ")

        if (pwd_ck != pwd_c):
            print("비밀번호가 일치하지 않습니다.\n")
            continue

        idf = open("id.txt",'w') # 아이디 설정
        idf.write(id_c)
        idf.close()

        pwdf = open("pwd.txt", 'w') # 비밀번호 설정
        pwdf.write(pwd_c)
        pwdf.close()

        moneyf = open("money.txt", 'w') # 기본 자금 설정
        moneyf.write("1000000") # 기본 금액 100만원으로 설정
        moneyf.close()

        smuf = open("smu.txt", 'w') # 주가 설정
        smuf.write("10000") # 기본 주가 1만원으로 설정
        smuf.close()
        samf = open("sam.txt", 'w') # 주가 설정
        samf.write("10000") # 기본 주가 1만원으로 설
        samf.close()
        
        break # 회원가입 성공

def log_in(): # 로그인 함
    while True: # 로그인 정보가 일치할 때까지 반
        print("< 로그인 >\n")
        id_in = input("아이디 입력 : ")
        pwd_in = input("비밀번호 입력 : ")

        id_r = open("id.txt", 'r')
        id_ck = id_r.read()
        id_r.close()
        
        pwd_r = open("pwd.txt", 'r')
        pwd_ck = pwd_r.read()
        pwd_r.close()
        
        if ((id_in != id_ck) or (pwd_in != pwd_ck)):
            print("아이디 또는 비밀번호를 잘못 입력하였습니다.\n")
            continue
        
        print("\n< 로그인 성공 >\n")
        break # 로그인 성공

def start_title(): # 게임 화면
        print("\n1. 매수")
        print("2. 매도")
        print("3. 리셋")
        print("4. 로그 아웃\n")
    
        smuf = open("smu.txt", 'r')
        smu_money = smuf.read()
        smuf.close()
        samf = open("sam.txt", 'r')
        sam_money = samf.read()
        samf.close()
    
        print("\n삼성전자 :", sam_money, "원")
        print("상명대학교 :", smu_money, "원\n")
        
def start(): # 게임 시작
    smu_s = 0 # 상명대학교 주식 개수
    sam_s = 0 # 삼성전자 주식 개수
    while True:
        
        print("--------------------------------------------------------------------------------")
        start_title()
        num = input("번호를 선택하십시오(1~4) : ") # 게임 동작
        print("--------------------------------------------------------------------------------")
        if ((num.isdecimal()) and (int(num) >= 0 and int(num) < 5)):
            num = int(num)
        else: # 동작 오류문
            print("다시 입력하십시오.\n")
            continue
            
        
        if (num == 1): # 매수
            while True:
                smuf = open("smu.txt", 'r')
                smu_money = smuf.read()
                smuf.close()
                samf = open("sam.txt", 'r')
                sam_money = samf.read()
                samf.close()

                smu_money = int(smu_money)
                sam_money = int(sam_money)
                
                moneyf = open("money.txt", 'r')
                money = moneyf.read()
                moneyf.close()

                money = int(money)
                
                print("잔액 :", money, "원\n")

                stock = input("주식 선택 : ")

                if (stock == "상명대학교"):
                    while True:
                        cnt = input("몇 주를 매수하시겠습니까? : ")

                        if(cnt.isdecimal() == False):
                            print("다시 입력하십시오.")
                            continue
                        
                        elif(int(cnt)*smu_money > money):
                            print("금액이 부족합니다.")
                            continue

                        cnt = int(cnt)
                        
                        smu_s = smu_s + cnt
                        money = money - (cnt*smu_money)
                        
                        moneyf = open("money.txt", 'w')
                        moneyf.write(str(money))
                        moneyf.close()
                        
                        break
                    
                elif (stock == "삼성전자"):
                    while True:
                        cnt = input("몇 주를 매수하시겠습니까? : ")

                        if(cnt.isdecimal() == False):
                            print("다시 입력하십시오.")
                            continue
                        
                        elif(int(cnt)*sam_money > money):
                            print("금액이 부족합니다.")
                            continue

                        cnt = int(cnt)
    
                        sam_s = sam_s + cnt
                        money = money - (cnt*sam_money)

                        moneyf = open("money.txt", 'w')
                        moneyf.write(str(money))
                        moneyf.close()
                        
                        break
                
                break
            
        elif (num == 2): # 매도
            while True:
                print("삼성전자:", sam_s, "주")
                print("상명대학교:", smu_s, "주\n")
            
                stock = input("주식 선택 : ")

                if (stock == "상명대학교"):
                    while True:
                        cnt = input("몇 주를 매도하시겠습니까? : ")

                        if ((cnt.isdecimal() == False) or (int(cnt) < 0)):
                            print("다시 입력하십시오")
                            continue

                        smu_s = smu_s - int(cnt)
                        break
                        
                elif (stock == "삼성전자"):
                    while True:
                        cnt = input("몇 주를 매도하시겠습니까? : ")

                        if ((cnt.isdecimal() == False) or (int(cnt) < 0)):
                            print("다시 입력하십시오")
                            continue

                        sam_s = sam_s - int(cnt)
                        break
                else:
                    print("다시 입력하십시오.\n")
                    continue

                break

        elif (num == 3): # 주가 리셋
            print("< 주가 리셋 >\n")

            smu_percent = random.randint(0, 100)
            sam_percent = random.randint(0, 100)

            # 상명대학교 주가 변동
            if (smu_percent <= 20): # 상승

                smuf = open("smu.txt", 'r')
                smu_money = smuf.read()
                smuf.close()

                smu_money = int(smu_money)
            
                smu_plus = random.randint(0, smu_money)
                smu_money = smu_money + smu_plus
                
                smuf = open("smu.txt", 'w')
                smuf.write(str(smu_money))
                smuf.close()
            
            elif (smu_percent > 20 and smu_percent <=40): # 하락

                smuf = open("smu.txt", 'r')
                smu_money = smuf.read()
                smuf.close()

                smu_money = int(smu_money)
                
                smu_minus = random.randint(0, smu_money)
                smu_money = smu_money - smu_minus

                if (smu_money < 0):
                    smu_money = 0
            
                smuf = open("smu.txt", 'w')
                smuf.write(str(smu_money))
                smuf.close()
            
            elif (smu_percent > 40 and smu_percent <= 50): # 많이 상승

                smuf = open("smu.txt", 'r')
                smu_money = smuf.read()
                smuf.close()

                smu_money = int(smu_money)
            
                smu_plus = random.randint(0, smu_money*5)
                smu_money = smu_money + smu_plus
                
                smuf = open("smu.txt", 'w')
                smuf.write(str(smu_money))
                smuf.close()
            
            elif (smu_percent > 50 and smu_percent <= 60): # 많이 하락

                smuf = open("smu.txt", 'r')
                smu_money = smuf.read()
                smuf.close()

                smu_money = int(smu_money)
            
                smu_minus = random.randint(0, smu_money*5)
                smu_money = smu_money - smu_minus

                if (smu_money < 0):
                    smu_money = 0
            
                smuf = open("smu.txt", 'w')
                smuf.write(str(smu_money))
                smuf.close()
            
            elif (smu_percent > 60 and smu_percent <= 90): # 랜덤으로 조금 변동

                smuf = open("smu.txt", 'r')
                smu_money = smuf.read()
                smuf.close()

                smu_money = int(smu_money)
            
                smu_t = random.randint(-(smu_money), smu_money)
                smu_money = smu_money + smu_t

                if (smu_money < 0):
                    smu_money = 0
            
                smuf = open("smu.txt", 'w')
                smuf.write(str(smu_money))
                smuf.close()
            
            else: # 유지
                pass

            # 삼성전자 주가변동
            if (sam_percent <= 20): # 상승

                samf = open("sam.txt", 'r')
                sam_money = samf.read()
                samf.close()

                sam_money = int(sam_money)
            
                sam_plus = random.randint(0, sam_money)
                sam_money = sam_money + sam_plus
                
                samf = open("sam.txt", 'w')
                samf.write(str(sam_money))
                samf.close()
            
            elif (sam_percent > 20 and sam_percent <=40): # 하락

                samf = open("sam.txt", 'r')
                sam_money = samf.read()
                samf.close()

                sam_money = int(sam_money)
            
                sam_minus = random.randint(0, sam_money)
                sam_money = sam_money - sam_minus

                if (sam_money < 0):
                    sam_money = 0
            
                samf = open("sam.txt", 'w')
                samf.write(str(sam_money))
                samf.close()
            
            elif (sam_percent > 40 and sam_percent <= 50): # 많이 상승

                samf = open("sam.txt", 'r')
                sam_money = samf.read()
                samf.close()

                sam_money = int(sam_money)
            
                sam_plus = random.randint(0, sam_money*5)
                sam_money = sam_money + sam_plus
                
                samf = open("sam.txt", 'w')
                samf.write(str(sam_money))
                samf.close()
            
            elif (sam_percent > 50 and sam_percent <= 60): # 많이 하락

                samf = open("sam.txt", 'r')
                sam_money = samf.read()
                samf.close()

                sam_money = int(sam_money)
            
                sam_minus = random.randint(0, sam_money*5)
                sam_money = sam_money - sam_minus

                if (sam_money < 0):
                   sam_money = 0
            
                samf = open("sam.txt", 'w')
                samf.write(str(sam_money))
                samf.close()
            
            elif (sam_percent > 60 and sam_percent <= 90): # 랜덤으로 조금 변동

                samf = open("sam.txt", 'r')
                sam_money = samf.read()
                samf.close()

                sam_money = int(sam_money)
            
                sam_t = random.randint(-(sam_money), sam_money)
                sam_money = sam_money + sam_t

                if (sam_money < 0):
                    sam_money = 0
            
                samf = open("sam.txt", 'w')
                samf.write(str(sam_money))
                samf.close()
            
            else: # 유지
                pass
            
        elif (num == 4): # 로그 아웃
            print("< 로그 아웃 >\n")
            break
        else:
            print("다시 입력하십시오.\n")
            continue
        
        




        
# 메인 함수 영역 -------------------------------------------------------------
while True:
    title()
    print("--------------------------------------------------------------------------------")
    choice = input("번호를 선택하십시오(1~3) : ")
    print("--------------------------------------------------------------------------------")

    if((choice.isdecimal() == True) and (int(choice) >= 0 and int(choice) < 4)):
        choice = int(choice)
        if(choice == 1):
            sign_up() # 회원 가입
        elif(choice == 2):
            log_in() # 로그인
            start() # 게임 시작
        elif(choice == 3):
            print("\t\t\t\t < 게임 종료 >")
            break # 게임 종료
    else: # 오류문
        print("다시 입력해 주세요!")
