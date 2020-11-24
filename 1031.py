a=[]
for i in range(20):
    if i in range(10):
        print("input x%d:"%(i+1),end=" ")
        x=eval(input())
        a.append(x)
    else:
        print("input x%d:"%(i+21),end=" ")
        x=eval(input())
        a.append(x)
print("input f1:",end=" ")
f1=eval(input())
print("input f2:",end=" ")
f2=eval(input())
print("input t:",end=" ")
t=eval(input())
print("1031声速测量 data analysis\n----------------------------------")
import math 
s=0
for i in range(10):
    s=s+(a[i+10]-a[i])/30
s=s/10
print("1:calculate lambda\ndx=%f\nlambda=%f"%(s,s*2))
sum=0
for i in range(10):
    sum=sum+((a[i+10]-a[i])/30-s)**2
sum=math.sqrt(sum/90)
print("ua(dx)=%f"%sum)
udx=math.sqrt(sum**2+(2.887e-3/30)**2+(5.774e-2/30)**2)
print("u(dx)=%f"%(udx))
print("u(lambda)=%f\n----------------------------------\n2:calculate f/u(f)"%(2*udx))

f_ave=0.5*(f1+f2)
df=0.5*(f2-f1)
uf=df/(math.sqrt(3))
print("u(f)=%f"%(uf))
print("f=%f,df=%f\n----------------------------------\n3:calculate v/u(v)"%(f_ave,df))

v=s*2*f_ave
vt=331.45*math.sqrt(1+t/273.15)
uvdivv=(((udx/s)**2)+(uf/f_ave)**2)**0.5
uv=uvdivv*v
wucha=abs((v-vt)/vt)
print("v=%f\nu(v)/v=%f\nu(v)=%f\n误差=%f"%(v,uvdivv,uv,wucha))
x=input("输入任意字符结束程序:")


