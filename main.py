from flask import Flask,request,Response
from flask_cors import CORS
import re
import os
import webbrowser
import xml.etree.ElementTree as ET

from Objeto import MODELO

REPORTE=[]
app=Flask(__name__)
#Cualquier IP
cors = CORS(app, resources={r"/*": {"origin": "*"}})


@app.route("/")
def inicio():
    return('<h1>CONSUMIENDO API</h1>')


#ESCRIBIENDO ARCHIVO DE SALIDA
@app.route('/events/', methods=['POST'])
def post_events():
    data = open('salida.txt', 'w+')
    data.write(request.data.decode('utf-8'))
    data.close()

    return Response(response=request.data.decode('utf-8'),
                    mimetype='text/plain',
                    content_type='text/plain')

#LEYENDO ARCHIVO DE SALIDA
@app.route('/events/', methods=['GET'])
def get_events():
    data = open('salida.txt', 'r+')
    return Response(response=data.read(),
                    mimetype='text/plain',
                    content_type='text/plain')

#RECIBIENDO CONTENIDO DEL ARCHIVO CARGADO
@app.route('/archivo/', methods=['POST'])
def analizando():
    print("-------SAVE CONSOLE---")
    content=request.data.decode('utf-8')
    print(content)
    #---------implementando lectura
    os.system('cls')
    try:
        re_email=r"[\w\.-]+@[\w\.-]+"
        re_fecha=r"(?:[0-9]{2}/){2}[0-9]{4}"
        re_codigo=r"[0-9]{5}"
        
        

        parkur=content.replace("<","").replace("EVENTO","<EVENTO").replace("/<EVENTO","</EVENTO")
    

        print("--------------------probando leer el parkur-------------------")
        print("este es mi parkur")
        print(parkur)
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
        print("REPORTADO validadas")
        print(val_users)
        print(contador2) #MESIRVE

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
        print("ERRORES validadas")
        print(val_errores)
        print(contador3)
    finally:
            #os.system('cls')
            print("     **************************      ")
            print("            SUCCESSFULLY             ")
            print("     **************************      ")
    data=ET.Element('ESTADISTICAS')
    items=ET.SubElement(data,'ESTADISTICA')
    x=0
    while x<len(validada):
        item1=ET.SubElement(items,'FECHA')
        item2=ET.SubElement(items,'CANTIDAD_MENSAJES')
        item1.text=str(validada[x])
        item2.text=str(contador1[x])
        item3=ET.SubElement(items,'REPORTADO_POR')
        xx=0
        while xx<len(validada):
            for i in repo[xx]:
                item4=ET.SubElement(item3,'USUARIO')
                item5=ET.SubElement(item4,'EMAIL')
                item6=ET.SubElement(item4,'CANTIDAD_MENSAJES')
                item5.text=str(i)
                item6.text=str(contador2[xx])
            xx+=1
        item7=ET.SubElement(items,'AFECTADOS')
        for k in afectados[x]:
            item9=ET.SubElement(item7,'AFECTADO')
            item9.text=k  
        item8=ET.SubElement(items,'ERRORES')
        zy=0
        while zy<len(val_errores):
            item10=ET.SubElement(item8,'ERROR')
            item11=ET.SubElement(item10,'CODIGO')
            item12=ET.SubElement(item10,'CANTIDAD_MENSAJES')

            item11.text=str(val_errores[zy])
            item12.text=str(contador3[zy]) 
            zy+=1    
        x+=1

    mydata=ET.tostring(data)
    ruta="estadística.xml"
    myfile=open(ruta,"wb")
    myfile.write(mydata)
    myfile.close()
    print("Ruta específicada: " + ruta)
    print("Se escribió el archivo satisfactorio")

    #--ESCRIBIENDO ARCHIVO
    data = open('entrada.txt', 'w+')
    data.write(request.data.decode('utf-8'))
    data.close()

    return Response(response=request.data.decode('utf-8'),
                    mimetype='text/plain',
                    content_type='text/plain')

#GENERANDO ARCHIVO
@app.route('/archivo/', methods=['GET'])
def mostrando():
    data = open('estadística.xml', 'r+')
    return Response(response=data.read(),
                    mimetype='text/plain',
                    content_type='text/plain')  

#RESETEANDO
@app.route('/reset/', methods=['POST'])
def RESET():
    global REPORTE
    REPORTE=[]

    return ("ok")
    

if __name__ =='__main__':
    app.run(debug=True,port=5000) 