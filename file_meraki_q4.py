data=open('merakipage4.txt','r')
content=data.read()
f=open('delhi.txt','w')
r=open('shimla.txt','w')
s=open('others.txt','w')

a=content.splitlines()
dict={}
for i in a:
    s=i.split()
    j=1
    value=''

    while j<len(s):
        if s[j]=='-':
            pass
        else:
            value=value+s[j]+''
        j=j+1
    dict[s[0]]=value


for k in dict:

    if dict[k]=='delhi':
        f=open('delhi.txt','a')
        f.write(k)
        f.write("\n")
        f.close()
 
        
    elif dict[k]=='shimla':

        r=open('shimla.txt','a')
        r.write(k)
        r.write("\n")
        r.close()
        
    else :
        s=open('others.txt','a')
        s.write(k)
        s.write("\n")
        s.close()