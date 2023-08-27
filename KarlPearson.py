# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def karlPearson(A, B):
    kp = 0
    Asum = 0
    Bsum = 0
    Amean = 0
    Bmean = 0
    for x in A:
        Asum += x
    for y in B:
        Bsum += y
    Amean = Asum/len(A)
    Bmean = Bsum/len(B)
    term1 = 0
    term2 = 0
    term3 = 0
    for i in range(0, len(A)):
        term1 += (A[i]-Amean)*(B[i]-Bmean)
        term2 += math.pow((A[i]-Amean), 2)
        term3 += math.pow((B[i]-Bmean), 2)
    
    kp = term1 / (math.sqrt(term2) * math.sqrt(term3))
    return kp
    

a = input("Physics score:")
b = input("History score:")
arr1 = list(map(int, a.strip().split()))
arr2 = list(map(int, b.strip().split()))

print("%.3f" % karlPearson(arr1, arr2))
