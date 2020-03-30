import xml.etree.ElementTree as et

tree=et.parse(r"structure02.xml")

root=tree.getroot()

for e in root.iter('name'):
    print(e.text)

for stu in root.iter('Student'):
    name=stu.find('name')

    if name!=None:
        name.set('test',name.text*2)

stu = root.find('Student')

e=et.Element('ADDer')
e.attrib={'a':'b'}
e.text='我加的'

stu.append(e)
# 一定要把修改的文件写入文件内
tree.write('structure02.xml')
