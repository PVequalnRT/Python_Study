# 유튜브 영상 배속하면 총 걸리는 시간 계산

# 사용자가 시간을 입력
# 시간 : 분 : 초 형태로 입력
# 분:초 형태

# 사용자로부터 배속 입력 받고
# 시간 계산해서 리턴
def calculator(*times):
    # 사용자에게 배속 입력받음
    a = float(input("원하시는 배속을 입력해주세요 :"))
    result = list()
    i = len(times) - 1

    while(0 <= i):
        if i == len(times) - 1:
            te = int(times[i])
            result.append(int(te/a))
        else:
            temp = str(float(times[i])/a)
            temp.split('.')
            result.append(int(temp[0]))
            result[len(result) - 1] += int(temp[1] * 60)
        i -= 1
    result.reverse()
    return result

# 사용자로부터 영상 시간 입력 받음
target = input("영상 시간을 입력해주세요 :").split(':')


# 영상시간이 시간포함일때
if len(target) == 3:
    result = calculator(target)
    print(result)

# 영상 시간이 시간 미포함일때
elif len(target) == 2:
    print("d2")

else:
    print("시간 입력 형식이 틀렸습니다.")

input()
