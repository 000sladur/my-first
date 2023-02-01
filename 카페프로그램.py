print("          =======                              ")
print("         l|                                    ")
print("         l|                                    ")         #카페 간판
print("         l|               -------------------  ")
print("         l|                  경민이의          ")
print("    =============                              ")
print("    |                               카페       ")
print("    |     c     |                              ")
print("    |     0     |         -------------------  ")
print("     |    f    |                               ")
print("     |    f    |                               ")
print("     |    e    |                               ")
print("     |    e    |                               ")
print("     |         |                               ")
print("     |         |                               ")
print("      =========                                ")



print("*************************************************")



print("        ============**menu**============               ")
print("         1번 . 아메리카노 (ame) *4000*                 ")
print("         2번 . 라떼       (lat) *4500*                 ")      #카페메뉴
print("         3번 . 에이드     (ade) *3000*                 ")
print("         4번 . 생과일주스 (jui) *2000*                 ")
print("         5번 . 아이스티   (ice) *2500*                 ")
print("         6번 . 머핀       (muf) *5000*                 ")
print("         7번 . 조각케이크 (cak) *8000*                 ")
print("         8번 . 허니브레드 (hon) *8500*                 ")
print("         0번 . *주문 안함*                             ")
print("         ================================              ")


ame = 1           
lat = 2
ade = 3                   #카페메뉴 변수 지정
jui = 4
ice = 5
muf = 6
cak = 7
hon = 8

ameMoney = 4000
latMoney = 4500         #카페메뉴 가격 변수 저장
adeMoney = 3000
juiMoney = 2000
iceMoney = 2500
mufMoney = 5000
cakMoney = 8000
honMoney = 8500




while True:    # 반복문
    money = int(input("돈을 넣어주세요: "))
    number = int(input("메뉴를 골라주세요"))

    if(number == 1):
        print("아메리카노는 4000원 입니다.")
        if money < ameMoney:
            print("돈이 부족합니다.")
        if money > ameMoney:
            print("           S      S              ")
            print("        S     S                  ")     # 아메리카노 주문
            print("        ---   -  -S              ")
            print("     -    S         -            ")
            print("     |  -      S     -  @@@      ")
            print("      |   - - -------  |   @     ")
            print("       |   americano  | @ @      ")
            print("        |            |@          ")
            print("         ------------            ")
            print("                                 ")
            print("                                 ")
            print("아메리카노 나왔습니다!!")
            print("거스름돈은",money - ameMoney,"입니다.")
            continue
    elif(number == 2):
        print("라떼는 4500원 입니다.")
        if money < latMoney:
            print("돈이 부족합니다.")
        if money > latMoney:
            print("         -------           ")
            print("       @         @         ")
            print("     @ \ \     \ \ @       ")
            print("   | \     \ \    \ |      ")     # 라떼 주문
            print("   |  \           \ |      ")
            print("   |   \         \  |      ")
            print("   |    \       \   @      ")
            print("    @     \ \  \   @       ")
            print("     @    latte  @         ")
            print("       @--------           ")
            print("                           ")
            print("라떼 나왔습니다!!")
            print("거스름돈은", money - latMoney,"입니다.")
            continue
    elif(number == 3):
        print("에이드는 4500원 입니다.")
        if money < adeMoney:
            print("돈이 부족합니다.")
        if money > adeMoney:
            print("            ===         ")
            print("           =            ")
            print("       ___= ___         ")   # 에이드 주문
            print("      | #   # |         ")
            print("      |  *   *|         ")
            print("       |   # |          ")
            print("       | *  *|          ")
            print("       | #   |          ")
            print("       |   # |          ")
            print("       |*   *|          ")
            print("        =====           ")
            print("        aide            ")
            print("에이드 나왔습니다!!")
            print("거스름돈은", money - adeMoney,"입니다.")
            continue
    elif(number == 4):
        print("생과일주스는 2000원입니다.")
        if money < juiMoney:
            print("돈이 부족합니다.")
        if money > juiMoney:
            print("          +               ")
            print("          +               ")
            print("      @@@ +               ")
            print("     @###@   |            ")   # 생과일주스 주문
            print("      |&&&&&&|            ")
            print("      |&&&&&&|            ")
            print("      |&&&&&&|            ")
            print("      | &&&& |            ")
            print("      | juice|            ")
            print("       ======             ")
            print("생과일 주스 나왔습니다!!")
            print("거스름돈은", money - juiMoney, "입니다.")
            continue
    elif(number == 5):
        print("아이스티는 2500원입니다.")
        if money < iceMoney:
            print("돈이 부족합니다.")
        if money > iceMoney:
            print("                           ")
            print("      _______              ")
            print("     |_______|             ")
            print("     |  ㅁ   |--           ")
            print("     |ㅁ  ㅁ |  |          ")    #아이스티 주문
            print("     |   ㅁ  |  |          ")
            print("     | ㅁ ㅁ |  |          ")
            print("     | ㅁ    |--           ")
            print("     |  ㅁ   |             ")
            print("     | ㅁ    |             ")
            print("       |   |       icetea  ")
            print("        | |                ")
            print("    ___|   |___            ")
            print("아이스티 나왔습니다!!")
            print("거스름돈은", money - iceMoney, "입니다.")
            continue
    elif(number == 6):
        print("머핀은 5000원 입니다.")
        if money < mufMoney:
            print("돈이 부족합니다.")
        if money > mufMoney:
            print("        =========            ")
            print("      =   ㅁ  ㅁ =           ")
            print("     = ㅁ  ㅁ    ㅁ=         ")
            print("    |++++++++++++++|         ")
            print("    |              |         ")   # 머핀 주문
            print("     |            |          ")
            print("     |            |          ")
            print("      =============          ")
            print("      _____________          ")
            print("머핀 나왔습니다!!")
            print("거스름돈은", money - mufMoney, "입니다.")
            continue
    elif(number == 7):
        print("조각케이크는 8000원 입니다.")
        if money < cakMoney:
            print("돈이 부족합니다.")
        if money > cakMoney:
            print("                           ")
            print("  cake                     ")
            print("              = )          ")
            print("          = =    )         ")
            print("       = =        )        ")    #조각케이크 주문
            print("      =____________)       ")
            print("     |              |      ")
            print("     | ============ |      ")
            print("    @| ============ |@     ")
            print("   @ |______________| @    ")
            print("   @                  @    ")
            print("     @@@@@@@@@@@@@@@@@     ")
            print("조각케이크 나왔습니다!!")
            print("거스름돈은",money - cakMoney, "입니다.")
            continue
    elif(number == 8):
        print("허니브레드는 8500원 입니다.")
        if money > honMoney:
            print("돈이 부족합니다,")
        if money > honMoney:
            print("             @                ")
            print("            @  @@ @           ")
            print("          @  @  @ ++@+++=|    ")
            print("       =@   @    @ @ @ = |    ")   # 허니브레드 주문
            print("      |++++++++++++++|=  |    ")
            print("      |              |   |    ")
            print("      |  |           |  =|    ")
            print("      |  | ______    | =      ")
            print("      |______________|=       ")
            print("                              ")
            print("     honeybread               ")
            print("허니브레드 나왔습니다!!")
            print("거스름돈은", money - honMoney, "입니다.")
    elif(number == 0):
            break
    else :
            print("없는 번호입니다. 다시 입력해주세요")           #없는번호 일때
            continue
    
            
               
            



























            
        

   
        
   











     
            




    
    
    
    





                
    












