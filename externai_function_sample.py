#외장함수 검색 : list of python index
# glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
import glob
print(glob.glob(".py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())



# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
import datetime
# print("오늘 날짜는 ", datetime.date.today())
# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()   #오늘 날짜 저장
td = datetime.timedelta(days=100)   # 100일 저장
print("우리가 만난지 100일은", today+td)    # 오늘부터 100일 후
# life_time = input("%Y-%m-%d")
# left_time = life_time-today
# print("남은 수명은 : {0}".format(left_time))
