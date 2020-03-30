import xml.etree.ElementTree

root=xml.etree.ElementTree.parse("structure01.xml")
print("利用getiterator访问")
nodes=root.getiterator()
for node in nodes:
    print("{0}--{1}".format(node.tag,node.text))

print("利用find和findall方法： ")
ele_Student=root.find("Student")
print("{0}--{1}".format(ele_Student.tag,ele_Student.text))

ele_Students=root.findall("Student")
for ele in ele_Students:
    print("{0}--{1}".format(ele.tag, ele.text))
    if "desc" in ele.attrib.keys():
        print(ele.attrib['desc'])
    for sub in ele.getiterator():
        if sub.tag=="name":
            print("{0}--{1}".format(sub.tag, sub.text))

