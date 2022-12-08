import random
from text_unidecode import unidecode

# 3.-kod  aleyatwa alfabetik san repetisyon
alfa1="abcdefghijklmnopqrstuvwxyz"

def aleyatwa1(alfa,nomb):
    return "".join(random.sample(alfa,nomb))


kod1=aleyatwa1(alfa1,10)
print(kod1)
print(len(kod1))


# 4.-kod aleyatwa alfanimerik san repetisyon

alfa2="abcdefghijklmnopqrstuvwxyz1234567890"

def aleyatwa2(alfa,nomb):
    return "".join(random.sample(alfa,nomb))


kod2=aleyatwa2(alfa2,36)
print(kod2)
print(len(kod2))

# 5.-jenere yon SLUG 

alfa3="yon c'henn pou fé\slug"
def slug(alfa: str):
    uni=unidecode(alfa)
    ch=""
    for i in range(len(uni)):
        if uni[i] == "\'" :
            ch += ""
        elif uni[i].isalnum() == False:
            ch += "-"
        elif uni[i].isalnum() == True:
            ch += uni[i]
    return ch
print(slug(alfa3))