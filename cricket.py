ball=0
dic={}
overs=2
a=[]
extra_run=0
total_run=0

Nb=[]
Wd=[]

wkt=0
wicket={"p1":False,"p2":False,"p3":False}
ply1=[]
ply2=[]
ply3=[]
p1=True
p2=False
p3=False



def No_ball(nb):
  Nb.append(nb)
  if p1:
    ply1.append(int(b[0]))
  if p2:
    ply2.append(int(b[0]))
  if p3:
    ply3.append(int(b[0]))
    

def Wide_Ball(wb):
  Wd.append(wb)
    
  if p1:
    ply1.append(int(b[0]))
  if p2:
    ply2.append(int(b[0]))
  if p3:
    ply3.append(int(b[0]))   
   
def change_p1():
  ply1.append(int(b))
  if wicket["p2"]:
    p2=False
    p3=True
    p1=False
    print(p1,p2,p3)
  else:
    p2=True
    p1=False 
    print(p1,p2,p3)
   

def change_p2():
  ply2.append(int(b))
  if wicket["p1"]:
    p1=False
    p3=True
    p2=False
    print(p1,p2,p3)
  else:
    p2=False
    p1=True 
    print(p1,p2,p3)

while (ball<4):
  b=(input())

  try:
    a.append(int(b))
    total_run+=int(b)
    if p1:      
      if ( int(b)==1 or int(b)==3):
        change_p1()
        '''ply1.append(int(b))
           if wicket["p2"]:
          p2=False
          p3=True
          p1=False
        else:
          p2=True
          p1=False ''' 
      else:
        ply1.append(int(b))

    elif p2:
      if (int(b)==1 or int(b)==3):
        
        change_p2()
        '''ply2.append(int(b))
        if wicket["p1"]:
          p1=False
          p3=True
          p2=False
        else:
          p2=False
          p1=True  '''
         
      else:
        ply2.append(int(b))  

    elif p3:
      if (int(b)==1 or int(b)==3):
        ply3.append(int(b))
        p3=False
        if wicket["p1"]:
          p1=False
          p2=True
        if wicket["p2"]:
          p2=False  
          p1=True
         
      else:
        ply3.append(int(b))     
    else:
      pass   
     
  except:

    a.append((b))
    extra_run=extra_run+int(b[0])
    total_run+=int(b[0])

    if b[1:]=="wkt":
      wkt=wkt+1
      if p1:
        wicket["p1"]=p1
        p1=False
        p3=True
        
      if p2:
        wicket["p2"]=p2
        p2=False
        p3=True
          
    if b[1:]=="nb":    
      No_ball(int(b[0]))
      continue
    if b[1:]=="wd":
      Wide_Ball(int(b[0]))
      continue
  ball=ball+1   





print(f"Total Runs Scored: {total_run},\nNumber of wickets: {wkt}, \nExtras: {extra_run},\nWide Ball: {sum(Wd)},\nNo Ball: {sum(Nb)}")
print(f"Score by batesman:\n 1st batsman: {sum(ply1)} runs; \n 2nd batsmen: {sum(ply2)} runs;\n 3rd batsmen: {sum(ply3)} runs.")



