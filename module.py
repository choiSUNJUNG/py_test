#일반 가격
def price(people):
    # print("{0}, {1}원 입니다.".format(people, people* 10000))
    print("{0}명 가격은 {1}원 입니다.".format(people, people* 10000))
    print("{:,}".format(people * 10000))
#조조 할인
def price_morning(people):
    print("{0}명 조조할인 가격은 {1}원 입니다.".format(people, people* 6000))
#군인 할인
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people* 4000))
