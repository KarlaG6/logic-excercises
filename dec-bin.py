import numpy as np
# failed solo sirve pa enteros
def max_expo_required(dec):
    expo = 0 
    negative = False
    if dec<0:
        negative = True
        dec*=-1
    while 2**expo < dec:
        # print(str(2**expo < dec)+" "+ str(2**expo))
        expo +=1
    return expo
numie = -9.5
# print(numie)
# print(max_expo_required(numie))

#nop con este
def parteEntera_bin_c2(dec):
    expo = digits = min_num_bits_need(dec)
    num = r = 0
    reverse = ""
    num = dec
    res = []

    while num >= 2:
        # print(num)
        r = num%2
        res.append(r)
        num /= 2
        print(r)
    for x in range(len(res)-1, -1, -1):
        reverse += str(res[x]) 
    return reverse



# print(parteEntera_bin_c2(-14))

ex = 7.25
def dec_bin_c2_1(dec):
    reverse = digits = num = 0
    num = float(dec)
    res = []
    sign = dec<0
    numbody = {}
    base = 2
    #convertimos el num en string 
    num = str(num)
    
    #nos deshacemos el char del signo
    if sign:
        num = num[1:]
    #iterar para convertir num en array
    i = len(str(int(dec)*-1))
    i = i if sign else i- 1 
    #validamos e ingresamos el signo
    res.append(sign)
    numbody.update({str(base**i*-1): sign})
    for x in num:
        if x == ".":
            numbody.update({"pt": x})
        else:
            i -= 1
            numbody.update({str(base**i) : x})
        print(numbody)
        res.append(x)

    
    # creamos y llenamos las keys del dict 
    # i = 1
    # while i<=len(res):

    
    #recorremos el array validando que no sea pt ni sign para convertirlo en int

    #converir el num en int y luego a str para extraer el numero de digitos
    digits = len(num)
    #crear un objeto con el indice y el valor
    

    print(res, numbody)
    
# dec_bin_c2(-14)
def dec_bin_float_pt(num, bits):
    aux = r = 0
    min_digits = min_num_bits_need(num)

    # convertir decimal a binario C2

        
    # Normalizar y representar


def dec_bin_c2(dec):
    expo = max_expo_required(dec)
    sign = dec<0
    numbody = {}
    aux = suma = 0
    suma = 2**expo*-1*sign
    numbody.update({str(2**expo*-1): sign})
    aux = suma + 2**expo
    while suma != dec:

        expo -= 1
        aux = suma + 2**expo
        numbody.update({str(2**expo) : dec >= aux})
        if dec >= aux:
            suma += 2**expo

    return numbody

print(dec_bin_c2(-7.25))
