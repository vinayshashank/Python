# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a,b = map(int,raw_input().strip().split(" "))
fact = math.factorial
print fact(a)/fact(b)/fact(a-b)
#--------------------------------------------------------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
result=[]
s = raw_input()
temp = re.sub(r'[^\sa-zA-Z]',"",s).lower().strip().split()
#print temp
for i in range(len(temp)):
    temp[i]="".join(sorted(temp[i]))
    
#print sorted(temp)
s2 = sorted(temp)
for i in s2:
    if i not in result:
        result.append(i)

print " ".join(result)
#--------------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=map(int,raw_input().strip().split(" "))

for i in range(b):
    if a%2==0:
        a=a/2
    else:
        a=3*a+1
print a
#---------------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
#import numpy as np
import math
c = map(float,raw_input().strip().split(" "))
v = map(float,raw_input().strip().split(" "))
v.append(1.0)

#c_np = np.array(c)
#v_np = np.array(v)

#z = np.dot(c_np,v_np)
z = sum(c[i]*v[i] for i in range(len(c)))

logit = 1.0/(1.0 + math.exp(-z))

print '%.3f' % (logit)
#-----------------------------------
