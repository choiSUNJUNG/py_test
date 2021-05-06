import time
print("날짜를 입력하세요.")
text = input("yyyy.mm.dd\n")
y, m, d = text.split('.')

print()
print("입력한 날짜는:")
print("{0}년 {1}월 {2}일 입니다.".format(y, m, d))