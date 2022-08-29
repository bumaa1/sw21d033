#n=int(input())# Гарсан тоо авлаа
n=10
s=5
for i in range(1,n+1,1): 
    if(n % i ==0):
        s = s * 1
        print(s,i)