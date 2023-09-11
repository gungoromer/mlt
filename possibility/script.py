from random import randint, choice
"""
a = randint(1,99)

print(a)

"""
"""
#A olayının olma olasılığı
a= randint(1,100)

if a<=15:
    print("olay gerçekleşti")
else:
    print("olay gerçekleşmedi")

"""

"""
#bir listenin içinden seçim
list = ["A","B","C","D"]

secim = choice(list)

print(secim)
"""
"""
#a olayının olma olasıılığı %15 tir.
#B olayının olma olasılığı %30dur. 


count =0
for i in range(10000):
    a= randint(1,100)
    b= randint(1,100)
    if a<=15 and b<=30:
        count +=1

print("a ve bnin olma olasılığı", 100* count/10000)
"""


"""
#iki zarın toplamının 9dan büyük olma olaslığı

count =0
for i in range(10000):
    zar1= randint(1,6)
    zar2= randint(1,6)
    sum = zar1 + zar2 
    if sum>9:
        count+=1

print("iki zarın toplamının 9 dan büyük olma olasılığı: ", 100 * count / 10000)

"""


"""
Bir çantada 3 madeni para vardır. Bunlardan ikisi normal ve üçüncünün iki tarafında da yazı vardır.
Bir para rastgele seçiliyor ve 4 kez atılıyor. 4 defada yazı gelirse bunun üçüncü para olma olasılığı nedir. ?
"""

sart1, sart2 = 0,0
para1 =["yazi","tura"]
para2 =["yazi","tura"]
para3 =["yazi","yazi"]

list = [para1,para2,para3]



for i in range(10000):
    chosen=choice(list)
    count =0
    for j in range(4):
        yaziTura= choice(chosen)
        if yaziTura=="yazi":
            count+=1
    if count == 4:
        sart1+=1
        if chosen ==para3:
            sart2+=1


print("Olasılık:", 100* sart2 / sart1)