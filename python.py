

ball=0
dic={}
overs=2
a=[]
extra_run=0
total_run=0
NB=0
wkt=0
while (ball<12):
  b=(input())
  try:
    a.append(int(b))
    total_run+=int(b)

  except:
    a.append((b))
    extra_run=extra_run+int(b[0])
    total_run+=int(b[0])

    if b[1:]=="wkt":
      wkt=wkt+1
    if b[1:]=="nb":      
      continue  
    if b[1:]=="wd":      
      continue  
  ball=ball+1   
