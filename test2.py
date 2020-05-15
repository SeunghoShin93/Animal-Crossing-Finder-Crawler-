
x = 'name'
cnt = 0
globals()[x+str(cnt)] = 5

print(globals()[x+str(cnt)])

def plus():
    global cnt
    cnt+=1
plus()
print(cnt)