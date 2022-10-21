s0=1
s1=1

N=int(input('Введіть кількість сходинок: '))
if N<2:
       print(1)
else:
       for i in range(2, N+1):
              sN=s0+s1
              s0=s1
              s1=sN
       print('SN=', sN)