from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Items(BaseModel):
    name:str
    sno:int
    marks:list
    std:dict

@app.post("/pydantic")
def pydantics(x:Items):
    return x

def is_prime(n:int):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return "prime"
    else:
        return "Not Prime"
    

@app.get("/First")
def read_root():
    i=1000
    return i
@app.post("/post_1")
def trash(x:int):
    y=x+100
    z=read_root()
    return [x,y,z]

@app.get("/check_prime")
def is_prime(n:int):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return "prime"
    else:
        return "Not Prime"
    
@app.post("/str")
def fun_str(st:str):
    return str

@app.post("/ex1")
def student_details(sn:str, sno:int, su:str, sp:str):
    # lenn=len(sp)
    # l=["*" for i in range(1,lenn+1)]
    # y="".join(l)
    dic={"student name":sn,"student number":sno,"user name":su,"student password":"*"*len(sp)}
    # return sn,sno,su,"*"*len(sp)
    return dic