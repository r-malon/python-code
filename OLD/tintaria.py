area= float(input("Digite a área: "))
tinta=area/6
lata=tinta//18
gal=tinta/4#não lembro como era o problema original
if 12 <= tinta <= 18:
    print("Você usou 1 lata e vai pagar R$ 80!!!")
elif tinta%18 <= 12:
    print("Você usou",lata,"latas, 3 galões e vai pagar R$",(lata*80)+(gal*25))    
elif tinta <= 4:
    print("Você usou 1 galão e vai pagar R$ 25!!!")
