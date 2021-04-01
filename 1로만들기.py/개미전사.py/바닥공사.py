정수 x가 주어졌을 때 정수 x에서 사용할 수 있는 연산은 다음과 같이 4가지이다.
1) x가 5로 나누어떨어지면 5로 나눈다.
2) x가 3으로 나누어떨어지면 3으로 나눈다.
3) x가 2로 나누어 떨어지면 2로 나눈다.
4) x에서 1을 뺀다.

x = int(input())
#앞서 계산한 결과를 저장하기 위한 dp테이블 초기화
d=[0]*30001
for i in range(2,x+1):
  d[i] = d[i-1]+1

  if i%2==0:
    d[i] = min(d[i],d[i//2]+1)
  if i%3==0:
    d[i] = min(d[i],d[i//3]+1)
  if i%5 == 0:
    d[i] = min(d[i],d[i//5]+1)
for i in range(x+1):
  print(d[i],end=' ')
  
  
  
  
#개미전사

n = int(input())
data = list(map(int,input().split()))

d = [0]*100

d[0] = data[0]
d[1] = max(data[0],data[1])
for i in range(2,n-1):
  d[i] = max(d[i-1],d[i-2]+data[i])

print(d[n-1])


#가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다. 이 얇은 바닥을 1*2, 2*!,2*2의 덮개를 이용해 채우고자 한다.
이때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오

































