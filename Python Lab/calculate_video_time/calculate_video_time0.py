# 유튜브 영상 배속하면 총 걸리는 시간 계산
#시간 계산 함수
def calc(*times):
    a = float(input("배속을 입력해 주세요 :"))
    i = len(times) - 1
    result = list()
    while(i >= 0):
        if i == len(times) - 1:
            result.append(round(times[i] / a, 2))
            print(result)
        else:
            temp = str(round(times[i] / a, 1)).split('.')
            result[len(result) - 1] += int(temp[1]) * 6
            result.append(int(temp[0]))
        i -= 1
    result.reverse()
    return result


# 사용자가 시간을 입력
# 시간 : 분 : 초 형태로 입력
# 분:초 형태
target = list(map(int,input("영상 시간을 입력해주세요 :").split(':')))

if len(target) == 3:   #시 분 초 형식으로 입력 되면
    result = calc(target[0],target[1],target[2])
    print(result[0],"시간",result[1],"분",result[2],"초 걸립니다.")

elif len(target) == 2:  #분 초 형식으로 입력 되면
    result = calc(target[0], target[1])
    print(result[0],"분",result[1],"초 걸립니다.")

else:
    print("입력 형식이 틀렸습니다. 콤마를 이용해주세요.")
