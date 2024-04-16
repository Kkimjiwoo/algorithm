# -*- coding: utf-8 -*-
"""알고리즘(1장~5장).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M9Vg8wxMYBrnqLfsIrEOQcJ_Xg8xGAoE

# 알고리즘
- 어떤 문제를 풀기 이한 절차나 방법
- 주어진 '입력'을 '출력'으로 만드는 과정
- 각 단계는 구체적이고 명료해야 함

1. 1부터 N까지 합 구하기 이론
"""

# 0.1 절댓값 구하기 알고리즘
import math # 수학 모듈 사용


# 절댓값 알고리즘 1(부호 판단)
# 입력: 실수 a
# 출력: a의 절댓값
def abs_sign(a):
  if a >= 0:
    return a
  else:
    return -a

print(abs_sign(-6))
print(abs_sign(5))

# 절댓값 알고리즘 2(제곱-제곱근)
def abs_square(a):
  b=a*a
  return math.sqrt(b) # 수학모듈의 제곱근 함수

print(abs_square(-15))
print(abs_square(6))

"""1.1 알고리즘 기초"""

# 1부터 n까지 합 구하기

# 1부터 n까지 연속한 숫자의 합 구하기
def input_num(a):
  sum =0
  for i in range(1,a+1):
    sum += i
  return sum

input_num(100)

# other way
# 가우스의 반분법 n(n+1)/2
# 이공식을 이용하여 1부터 n까지 연속한 합을 구하는 알고리즘
def sum_num(n):
  return n*(n+1)//2  # 정수 나눗셈을 의미 , '/'을 사용하면 .0으로 표현

print(sum_num(100))

# 주어진 문제를 푸는 여러가지 방법이 존재
# 어떤게 더 편안하고 쉬운지 판단하기
# 입력크기와 계산 횟수의 관계 생각하

"""대문자 O표기법: 계산 복잡도 표현
- 계산 복잡도: 어떤 알고리즘이 문제를 풀기 위해 해야 하는 계산이 얼마나 복잡한지를 나타낸 정도
- 그 중 대문자 O표기법을 많이 사용 (빅오)
---
- 첫 번째 알고리즘은 입력 크기 n에 대해 사칙 연산(덧셈)을 n번 해야 함
- 이때 이 알고리즘의 계산 복잡도를 O(n)이라고 표현
- 필요한 계산 횟수가 입력 크기에 정비례할 때도 O(n) 이라고 표현
---
- 두 번째 알고리즘은 입력 크기 n과 무관하게 사칙연산을 세 번 해야 함
- 이때 알고리즘 계산 복잡도는 O(1)로 표기
- 입력크기가 n과 필요한 계산의 횟수가 무관하다면, 즉 입력크기가 커져도 계산 시간이 더 늘어나지 않는다면 O(1)로 표기
- 첫 번째 알고리즘에서 O(2n)을 O(n)으로 표현하는 것과 같은 원리


"""

# 대문자 O표기법은 알고리즘의 대략적인 성능을 표시하는 방법
# 세밀한 계산 횟수나 소요시간을 표현하는 것이 아님
# 입력크기 n과 필요한 계산 횟수와의 '관계'에 더 주목하는 표현
# 입력크기가 큰 문제를 풀 때는 보통 O(1)인 알고리즘이 훨씬 더 빠름
# --> O(n) 필요한 계산 획수가 입력 크기 n과 비례할 때
# --> O(1) 필요한 계산 횟수가 입력 크기 n과 무관할

"""계산 복잡도
1. 시간 복잡도
- 어떤 알고리즘을 수행하는 데 얼마나 오랜 시간이 걸리는지 분석한 것
- 사칙연산 횟술 계산 복잡도를 생각해 본 것은 시간 복잡도에 해당
- 어떤 알고리즘을 수행하는 데 필요한 사칙연산의 횟수가 많아지면 결국 알고리즘 전체를 수행하는 시간이 늘어나기 때문

2. 공간 복잡도
- 어떤 알고리즘을 수행하는 데 얼마나 많은 공간(메모리/기억장소)이 필요한지 분석한
"""

# 1-1 1부터 n까지 제곱의 합을 구하는 프로그램
def sum_sq(n):
  sum=0
  for i in range(1,n+1):
      sum=sum+i*i
  return sum

print(sum_sq(100))

# 곱셈 n번 , 덧셈 n번으로 사칙연산이 총 2n번 필요하지만 O(n)으로 표현
# 공식을 사용하면 O(1)

"""02. 최댓값 찾기"""

# list 개념

## len(a)
a=[]
print('a=',a)
print('len(a)=',len(a))
print('len([1,2,3])=', len([1,2,3]))

# append(x)
a=[1,2,3]
print('a=',a)
a.append(4)
print('a.append(4)=',a)

# insert(i,x)
a=[1,2,3]
print('a=',a)
a.insert(0,5)
print('a.insert(0,5)=',a)

# pop(i)
a=[1,2,3]
print('a=',a)
a.pop(-1)
print('a.pop(-1)=',a)

# clear()
a=[1,2,3]
print('a=',a)
a.clear()
print('a.claer()=',a)

# x in a
a=[1,2,3]
print('a=',a)
print('2 in a=', 2 in a)

,

# 주어진 숫자 n개 중 가장 큰 숫자를 찾는 알고리즘을 만들어 보세요
## 17,92,18,33,58,7,33,42
# 이 방법은 강사님의 방법보다 좋지 않음
# 돌리는 시간을 어떻게 줄일지를 생각해야함
num_list=[17,92,18,33,58,7,33,42]

def max_number():
  m=0
  i=0
  while i <len(num_list):
    for num_list[i] in num_list:
      if num_list[i] >= m:
        m=num_list[i]
    i +=1
  return m

max_number()

# other way(강사님)

def find_max(a):
  n= len(a)
  max_v=a[0]
  for i in range(1,n):
    if a[i] > max_v:
      max_v = a[i]
  return max_v

a=[17,92,18,33,58,7,33,42]
print(find_max(a))

"""최댓값 구하기 프로그램의 계산 복잡도(시간복잡도)
- 최댓값을 구하는 데 컴퓨터가 해야 하는 가장 중요한 계산은 두 값 중 어느 것이 더 큰지를 판단하는 '비교'
- 위 프로그램은 반복문 안에 if문이 있어 자료 n개 중에서 최댓값을 찾으려면 비교를 n-1번 해야함
- 계산 복잡도는 O(n-1)이 아닌 O(n)
- 계산 복잡도의 가장 중요한 특징은 입력 크기와 계산 시간이 대체로 비례
"""

# 리스트에 숫자 n개 있을 때 가장 큰 값이 있는 위치 번호를 돌려주는 알고리즘

def idx(a):
  n= len(a)
  max_idx=0  # 리스트 중 0번 위치를 최댓값의 위치로 기억
             # (for 문을 돌면서 0번 위치의 값보다 큰 값이 있다면 변수가 바뀌게 알고리즘 작성)
  for i in range(1,n):
    if a[i] > a[max_idx]:
      max_idx = i
  return max_idx

a = [17,92,18,33,58,7,33,42]
print(idx(a))

# 리스트에 숫자 n개 있을 때 가장 작은 값이 있는 위치 번호를 돌려주는 알고리즘

def idx(a):
  b = len(a)
  min_idx = 0
  for i in range(1,b):
    a[i]<a[min_idx]
    min_idx = i
  return min_idx

a = [17,92,18,33,58,7,33,42]
print(idx(a))

"""03. 동명이인 찾기 1"""

# 집합set 개념

## 집합: 리스트와 같이 정보를 여러개 넣어서 보관할 수 있는 파이썬 기능
## 집합 하나에 같은 자료가 중복되어 들어가지 않고, 자료의 순서도 의미가 없다는 점이 리스트와 다름

s = set()
s.add(1)
s.add(2)
s.add(2)                  # 이미 2가 집합에 있으므로 중복해서 들어가지 않음
print('s=',s)
print('len(s)=',len(s))   # 집합 s에는 자료가 두 개 들어 있
{1,2} == {2,1}            # 자료의 순서는 무관하므로 같은 집합

# discard()
print('s=',s)
s.discard(2)
print('s.discard(2)=>',s)

# clear()
s = {1,2,3}
print('s=',s)
s.clear()
print('s.clear()=>',s)  # clear은 빈 집합이 됨

# x in s
s={1,2,3}
print('s=',s)
print('2 in s =>',2 in s) # 2가 집합 s 안에 없으므로 true

,# n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘

## 여러 사람의 이름중에서 같은 이름이 있는지 확인
## 같은 이름이 있다면 깉은 이름들을 새로 만든 결과 집합에 넣어 돌려주면 됨
## 입력은 n명의 이름이 들어 있는 리스트
## 결과는 같은 이름들이 들어 있는 집합 set


def samename(a):
    n= len(a)
    res = set()
    for i in range (0,n-1):  # 0부터 n-2까지 반복
      for j in range(i+1,n): # i+1부터 n-1까지 반복
        if a[i] == a[j]:
          res.add(a[i])
    return res

name = ['tom','jerry','mike','tom']
print(samename(name))
# i 는 첫번째의 tom부터 mike까지만 돌아감
# tom은 j반복문에 의해 jerry, mike, tom 3명만 돌림
# i=1은 jerry, 두번째 반복문에서 j=2부터 돌림 즉, jerry는 mike와 tom 까지 비교

name = ['tom','jerry','jerry','mike','tom']
print(samename(name))

# 중첩된 반복문
## 리스트 안의 자료를 서로 빠짐없이 비교하되 중복해서 비교하지 않게 함

"""알고리즘 분석
- 0번 위치는 n-1, 1번 위치는 n-2, ...,n-1위치는 0번 비교로 전체 비교 횟수는 0+1+...+(n-1)
- 1부터 n 까지의 합 구하는 공식 n*(n+1)/2를 이용하여 n(n-1)/2
- n(n-1)/2 번 비교해야 함
- 대문자 O표기법으로는 O(n^2)이라고 표현(n의 제곱에 비례해서 계산 시간이 변하는 것이 핵심)

- 계산 복잡도가 O(n^2)인 알고리즘은 입력크기 n이 커지면 계산시간은 그 제곱에 비례함로 엄청난 차이로 증가

"""

# 두 명을 뽑아 짝으로 만드는 프로그램
## n명에서 두 명을 뽑아 짝을 만드는 모든 경우를 찾는 프로그램
## 입력: n명의 이름이 들어 있는 리스트
## 출력: 두 명을 뽑아 만들 수 있는 모든 짝

def print_pairs(a):
  n= len(a)
  for i in range(0,n-1):
    for j in range(i+1,n):
      pair = print(a[i],'-',a[j])
  return pair

name = ['jiwoo','bh','je','hj','hk']
print_pairs(name)

# n 명에서 두 명을 뽑아 짝으로 만들면 짝 조합이
## 0번 째 사람은 n-1/.../i에서 마지막 n-2번째 사람은 1번
## 조합이 n(n-1)/2가지 출력

"""대문자 O표기법
- 65536 -> O(1)
- n-1   -> O(n)
- 2n^(2) + 100n -> O(n^2)

# 재귀호출
04. 팩토리얼 구하기
"""

# 1부터 n까지 연속한 정수의 곱을 구하는 알고리즘을 만들기

def fact(n):
  f=1                     # 곱을 계산할 변수, 초깃값
  for i in range(1,n+1):  # 1부터 n까지 반복(n+1은 제외)
    f = f*i               # 곱셈 연산으로 수
  return f

print(fact(1))
print(fact(5))

"""재귀호출
- 어떤 함수 안에서 자기 자신을 부르는 것

"""

def hello():
  print('hello')
  # hello()  #-> 무한 반복

hello()

# hello를 계속 출력하다가 함수 호출에 필요한 기억 장소를 다 써버리면
# 에러가 나고, 정지 -> 올바른 재귀함수 아님
# 반복을 멈추려면 ctrl + c

"""- 재귀 호출 프로그램이 정상적으로 작동하려면 종료 조건이 필요
- 즉, 특정 조건이 되면 자신을 호출하지 않고 멈추도록 설계
- 재귀 호출 함수가 계산 결과를 돌려줄 때는 return 명령을 사용해서 종료, 조건의 결과값부터 돌려줌
- 종료 조건의 결과값은 마지막으로 호출된 함수의 결과값
"""

# 팩토리얼을 구하는 알고리즘

## 연속한 숫자의 곱을 구하는 알고리즘

def fact(n):
  if n <= 1:          # n이 1 이하인지 비교, 이때 1을 결과값으로 돌려
    return 1
  return n*fact(n-1)  # 함수 안에서 자기 자신을 또 부름
# 위의 조건에 따라 n이 1이 될때 재귀 호출을 멈춤


print(fact(5))

"""- 재귀 호출에는 종료 조건이 꼭 필요
- 종료 조건이 없으면 재귀 에러나 스택 오버플로 등의 비정상적인 동작을 할 수도 있음
"""

# 연습문제 4-1
# 1부터 n까지의 합 구하기를 재귀 호출로 만들기

def sum_n(n):
  if n == 0:
    return 0  # 입력값이 0이다면 0을 출력
  return n + sum_n(n-1)   # 0이 아니다면 재귀함수를 이용하여 계속 출력

print(sum_n(10))

# 연습문제 4-2
# 숫자가 n개 들어 있는 리스트에서 재귀호출을 이용한 최댓값 찾기

def find_max(a,n):#a=[1,2,3], n = 3
  if n==1:        # 자료 값이 한개면 그 값이 최댓
    return a[0]     # 리턴 안됨
  max_n = find_max(a,n-1)  #max_n = find_max([1,2,3],2) = 3
  if max_n > a[n-1]:
    return max_n
  else:
    return a[n-1]

a= [81,68,95,74]
find_max(a, len(a))

"""5. 최대공약수 구하기"""

# 두 자연수 a와 b의 최대 공약수 구하는 알고리즘
## 두개 이상의 정수의 공통 약수 중에서 가장 큰 값
def gcd(a,b): # 입력 두개를 받
  i = min(a,b)    # 두 수 중에서 최솟값을 구하는 파이썬 함수
  while True:
    if a % i == 0 and b % i ==0:
      return i
    i = i -1 # i를 1만큼 감소

gcd(18,10)

gcd(18,10%18) # gcd(18,8) = gcd(8,18%8) = gcd(8,2) = gcd(2,8%2)= gcd(2,0)

# gcd(b,a%b)의 최대 공약수를 구하는 과정을 이용하는 재귀 호출 문제
# >> 좀 더 작은 값으로 자기 자신을 호출
# gcd(n,0)은 자기 자신이 최대 공약

# 유클리드 방식을 이용해 최대 공약수를 구하는 알고리즘

def gcd(a,b):
  if b == 0: # 어떤 수라도 유틀리드 방식을 이용하면 두번째 위치한 수가 0이 될 수 밖에 없음
  # 그때 b=0이 만족하면 최대 공약수는 a
    return a
  return gcd(b,a%b)  # 좀 더 작은 값으로 자기 자신을 호출0

print(gcd(1,5))
print(gcd(19,3))  # gcd(3,19 %3) = gcd(3,1) = gcd(1,3%1) =
print(gcd(19,4))  # gcd(4,19 %4) = gcd(4,3) = gcd(3,4%3)= gcd(3,1) = gcd(1, 1%3) =gcd(1,1) = gcd (1,1%1) = gcd(1,0)
print(gcd(2,4))

# 재귀 호출을 이용한 피보나치 수열 구하기
# 입력 n값(0부터 시작)

def fibo(n):  # fibo(4)
  if n <= 1:
    return n
  return fibo(n-2) + fibo (n-1)
fibo(7)

