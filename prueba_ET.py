import os
import xml.etree.ElementTree as ET

data=ET.Element('ESTADISTICAS')
items=ET.SubElement(data,'ESTADISTICA')

item1=ET.SubElement(items,'FECHA')
item2=ET.SubElement(items,'CANTIDAD_MENSAJES')
item3=ET.SubElement(items,'REPORTADO_POR')
item7=ET.SubElement(items,'AFECTADOS')
item8=ET.SubElement(items,'ERRORES')

item1.text='22/04/2021'
item2.text='3'


item4=ET.SubElement(item3,'USUARIO')
item5=ET.SubElement(item4,'EMAIL')

item9=ET.SubElement(item7,'AFECTADO')
item9.text='xx@ing.usac.edu.gt'

item10=ET.SubElement(item8,'ERROR')
item11=ET.SubElement(item10,'CODIGO')
item12=ET.SubElement(item10,'CANTIDAD_MENSAJES')

item11.text='2001'
item12.text='12'

item5.text='xx@ing.usac.edu.gt'
item6=ET.SubElement(item4,'CANTIDAD_MENSAJES')
item6.text='3'

mydata=ET.tostring(data)
ruta="prueba.xml"
myfile=open(ruta,"wb")
myfile.write(mydata)
myfile.close()
print("Ruta específicada: " + ruta)
print("Se escribió el archivo satisfactorio")