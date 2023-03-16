from pyautogui import press, click, moveTo, write, hotkey, locateOnScreen, locateCenterOnScreen, dragTo, doubleClick
from time import sleep
import csv
import pyperclip
import os

errlist = []
result = []

firstlist = ["읍면동","본번","부번","면적"]

# with open('result.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(firstlist)

with open('target.csv', newline='') as csvfile:
    target = csv.reader(csvfile)
    # count = 0
    # for i in target:
    #     count += 1
    # print("총개수 : ",count)
    # target = csv.reader(csvfile)
    ehd = ""
    for i in target:
        s = 0
        temp = []
        if(i[0] == "읍면동"):
            print("success!")
            os.system("pause")
        else:
            errorcheck = ""
            errorcheck2 = None
            errorcheck3 = None
            
            if(i[0][-1] == "산"):
                srts = i[0][0:-1] + " 산 " + i[1]
            else:
                srts = i[0] + " " + i[1]
            
            # srts = i[0] + " " + i[1] + "-" + i[2]
           
            print(srts + "-" + i[2])
            # pyperclip.copy(srts)
            if(ehd == i[0]):
                sleep(1)
            else:
                ehd = i[0]
                # y = input("검색?")
                print("검색?")
                os.system('pause >nul')

            moveTo(724, 360) # 본번 입력
            doubleClick()
            press('esc')
            write(i[1])
            
            sleep(0.5)

            moveTo(790, 361) #부번 입력
            if(i[2] == ''):
                doubleClick()
                press('backspace')
                # write(0)
            else:
                doubleClick()
                write(i[2])
                srts = srts + "-" + i[2]

            moveTo(894, 363) #검색버튼 클릭
            click()
            sleep(2)

            # 서치 이미지 없어질 때 까지
            while(locateOnScreen('searchimg.png')):
                pass

            sleep(2)

            if(locateOnScreen('nodata2img.png')):
                press('enter')
                temp.append(srts)
                temp.append(i[3])
                temp.append('필지 없음')
                with open('result.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(temp)
                print("필지 없음!")
                print("오류 목록 저장 완료")
            else:

                if(locateOnScreen('nodataimg.png')):
                    press('enter')
                else:
                    pass

                #마우스 드래그하기
                #마우스 드래그 시작 위치 이동
                moveTo(247, 703)
                dragTo(287,704,0.5, button='left')

                sleep(0.5)

                click(button='right')
                sleep(0.5)

                click(locateCenterOnScreen('copyimg.png'))

                s = pyperclip.paste()

                while(s == 0):
                    print('복사 실패')

                print('면적 : ',s)

                if(i[3] != s):
                    print("면적 상이!")
                    temp.append(srts)
                    temp.append(i[3])
                    temp.append(s)
                    result.append(temp)
                    with open('result.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(temp)
                    print("상이 목록 저장 완료")

for i in result:
    print(i)

print('면적 검토 완료!')






#             # moveTo(1241, 212) # 도스창 클릭
#             # click()
#             errorcheck = locateOnScreen('errorimg.png')
#             print("error is ", errorcheck)

#             if(errorcheck == None):
#                 while(True):
#                     sleep(0.1)
#                     errorcheck2 = locateOnScreen('printimg.png')
#                     if(errorcheck2 != None):
#                         print("error check 2 is", errorcheck2)
#                         break
#                     else:
#                         pass

#                 moveTo(835, 457)
#                 click()
#                 sleep(0.3)

#                 moveTo(771, 734)
#                 click()
#                 sleep(5)

#                 while(True):
#                     sleep(0.1)
#                     errorcheck3 = locateOnScreen('printimg2.png')
#                     if(errorcheck3 != None):
#                         print("error check 3 is", errorcheck3)
#                         break
#                     else:
#                         pass

#                 press('enter')

#                 # moveTo(492, 467)
#                 # click()
#                 pyperclip.copy(srts)
#                 sleep(1.5)
                
#                 # while(1):
#                 #     # 둘 중 하나라도 있을 때까지
#                 #     print("찾는 중")
#                 #     if(locateOnScreen('cverror.png') != None or locateOnScreen('cverror2.png') != None):
#                 #         break


#                 hotkey('ctrl', 'v')
#                 sleep(0.5)

            
#                 while(1):
#                     # 둘 다 없다면
#                     if(locateOnScreen('cverror.png') != None or locateOnScreen('cverror2.png') != None):
#                         hotkey('ctrl', 'v')
#                         sleep(0.5)
#                         print('다시 붙여넣기 합니다.')
#                     else:
#                         break
#                 print('복붙 성공!')
#                 press('enter')

#                 sleep(1)
#                 hotkey('ctrl', 'w')
#                 moveTo(1241, 212)
#                 click()
  
#             else:
#                 print("에러발생")
#                 errlist.append(i)
#                 click(locateCenterOnScreen('x.png'))

# print(errlist)
os.system('pause >nul')
