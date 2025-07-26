#IN THIS STAGE OF CODING WE GONA REACH TO HIGHST SKILL
def stain(name) :
    return name.replace(" ", "").lower()
def finum(number) :
    return int(float(number))
import time
def timer(a,b,c,s,t):
    for i in range(a,b,c):
        print(t)
        time.sleep(s)
print("Welcome To MasterLab")
print("MASTER,ILIYA,HOSSIEN")
proname=stain(input("What Is Your Name??(If Your Name Is On The List Above,Please Chose It From There)!! : "))
while proname!="iliya":
        proname=stain(input("Don’t Lie To Me. Just Tell Me Your Real Name. Rules Are Rules—it's Either Zero Or One..."))
print("Finally, Iliya is here in my MasterLab. In this place, we're going to analyze data and create some drops of knowledge! Cool, right? Do you want to see it?")
ans1=stain(input("For Start Do You Want Me To Analyze Your Number For You ?? (no,yes) :  "))
while ans1!="yes" and ans1!="no" :
    ans1=stain(input("Pleasse Anwser Me Only With(yes,no)"))
if ans1=="no" :
    print("oky",proname,"Good Luck")
    exit()
elif ans1=="yes" :
     ans2=finum(input("What Number Do Wanna Analyze ?? : "))
timer(5,0,-1,1,"Please Wait Analyze Statment .....")
B=[[0,0,0,0,0,0,0]]
A=[[2,3,5,7,9,11,13]]
for r in range(len(A[0])) :
    if ans2 % A[0][r]==0 :
        print("Looks Like Your Number Is divisble By",A[0][r],"And...")
        B[0][r]=A[0][r]
        time.sleep(1.7)
print("Hmm... According to my calculations, your number is totally divisible by",B,". Fascinating, isn’t it")


     
    
         
         
        
    

