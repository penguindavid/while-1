#input

n=int(input("digite el valor de n "))

#procesing

s=0
i=1

while i<=n:
    s=s+i
    i=i+1

print("la suma de los " + str (n)+"primeros numeros naturales es" + str (s) )