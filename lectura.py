import re
import os
import webbrowser
import xml.etree.ElementTree as ET

from Objeto import MODELO

REPORTE=[]

os.system('cls')
try:
    ruta="thor.xml"

    content=""

    with open(ruta, "r", encoding="utf-8") as f:
        content=f.read()
    #print(content)
    re_email=r"[\w\.-]+@[\w\.-]+"
    re_fecha=r"(?:[0-9]{2}/){2}[0-9]{4}"
    re_codigo=r"[0-9]{5}"
    
    nuevo={}

    parkur=content.replace("<","").replace("EVENTO","<EVENTO").replace("/<EVENTO","</EVENTO")
    #print("este es mi parkur")
    #print(parkur)

    print("--------------------probando leer el parkur-------------------")
    root = ET.fromstring(parkur)
    listado=[]
    for elemento in root:
        
        a=elemento.text
        b=a.rstrip()
        lineas=b.split("\n")
        event=[]
        for linea in lineas:
            fecha=re.findall(re_fecha,linea)
            correo=re.findall(re_email,linea)
            codigo=re.findall(re_codigo,linea)
            if correo!=[]:
                event.append(correo)
            elif fecha!=[]:
                parse=''.join(map(str,fecha))
                event.append(parse)
            elif codigo!=[]:
                parse=''.join(map(str,codigo))
                event.append(codigo)
            EVENTO=tuple(event)

        listado.append(EVENTO)
    print("--------------------OBJETOS-------------------")
    #separando datos para crear objetos
    for tupla in listado:
        objeto=[]
        usuarios=[]
        fecha=tupla[0] #FECHA
        repor=tupla[1][0] #REPORTADO POR
        for i in tupla[2]: #USUARIOS AFECTADOS
            #print(i)
            usuarios.append(i)
        codigo=tupla[3][0] #CODIGO
        REPORTE.append(MODELO(fecha,repor,usuarios,codigo))
    
    fechas=[]
    reportados=[]
    codigos=[]

    for i in REPORTE:
        fechas.append(i.fecha)
        reportados.append(i.reportado)
        codigos.append(i.codigo)
        print(i.fecha)
        print(i.reportado)
        print(i.afectados)
        print(i.codigo)
        print("------")


    #-----------VERIFICANDO FECHAS-------------------

    print(fechas)
    x=0
    validada=[]
    contador1=[]
    while x<len(fechas):
        if x==0:
            fecha=fechas[x]
            cantidad=fechas.count(fecha)
            validada.append(fecha)
            contador1.append(cantidad)
            print(cantidad)
        else:
            existe=False
            fecha=fechas[x]
            y=0
            while y<len(validada):
                if fecha==validada[y]:
                    existe=True
                    break
                else:
                    existe=False
                    y+=1
            if existe==False:
                cantidad=fechas.count(fecha)
                validada.append(fecha)
                print(cantidad)
                contador1.append(cantidad)
        x+=1
    print("fechas validadas")
    print(validada)
    print(contador1)

    #-----------VERIFICANDO USUARIOS QUE REPORTARON-------------------

    x=0
    val_users=[]
    contador2=[]
    while x<len(reportados):
        if x==0:
            reportado=reportados[x]
            cantidad=reportados.count(reportado)
            val_users.append(reportado)
            contador2.append(cantidad)
        else:
            existe=False
            reportado=reportados[x]
            y=0
            while y<len(val_users):
                if reportado==val_users[y]:
                    existe=True
                    break
                else:
                    existe=False
                    y+=1
            if existe==False:
                cantidad=reportados.count(reportado)
                val_users.append(reportado)
                contador2.append(cantidad)
        x+=1
    print("-----REPORTADO validadas")
    print(val_users)
    print(contador2)#MESIRVE


    repo=[]
    x=0
    while x<len(validada):
        temp=[]
        for i in REPORTE:
            if i.fecha==validada[x]:
                temp.append(i.reportado)
        repo.append(temp)       
        x+=1
    print("------REPORTADOS POR FECHA")
    print(repo)#MESIRVE

    #-------------------VERIFICANDO AFECTADOS-------------------
    afectados=[]

    x=0
    while x<len(validada):
        temp=[]
        for i in REPORTE:
            if i.fecha==validada[x]:
                for j in i.afectados:
                    temp.append(j)
        afectados.append(temp)       
        x+=1
    print("------AFECTADOS POR FECHA")  
    print(afectados)

    #-----------VERIFICANDO ERRORES REPORTADOS-------------------

    x=0
    val_errores=[]
    contador3=[]
    while x<len(codigos):
        if x==0:
            codigo=codigos[x]
            cantidad=codigos.count(codigo)
            val_errores.append(codigo)
            contador3.append(cantidad)
        else:
            existe=False
            codigo=codigos[x]
            y=0
            while y<len(val_errores):
                if codigo==val_errores[y]:
                    existe=True
                    break
                else:
                    existe=False
                    y+=1
            if existe==False:
                cantidad=codigos.count(codigo)
                val_errores.append(codigo)
                contador3.append(cantidad)
        x+=1
    print("--------ERRORES validadas")
    print(val_errores)
    print(contador3)
finally:
        #os.system('cls')
        print("     **************************      ")
        print("            SUCCESSFULLY             ")
        print("     **************************      ")