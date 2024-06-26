# 이진 검색 성능 확인 100000개 중에서 
# rendint 를 이용하여 무수한 데이터를 추출하여 이진 검색의 성능을 파악
## 함수
from random import randint, choice
def binSearch(ary, fdata) :
    global count
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end) :
        count += 1
        mid = (start + end) // 2
        if (ary[mid] == fdata) :
            pos = mid
            break
        elif (ary[mid] < fdata) :
            start = mid + 1
        else :
            end = mid - 1
    return pos

## 변수
count = 0
dataAry = [randint(0,100000000) for _ in range(1000000)]
dataAry.sort()
findData = choice(dataAry) # 할머니 키
# findData = 77

## 메인
print('배열-->', dataAry[:20])
position = binSearch(dataAry, findData)
if (position != -1) :
    print(findData,'는 ', position, '위치에 있음.(', count, '번)')
else :
    print(findData, '는 없어요ㅠ')

    
