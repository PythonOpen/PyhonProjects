import xml.dom.minidom
from xml.dom.minidom import parse

DOMTree=parse("structure01.xml")
doc=DOMTree.documentElement
# 显示子元素
for ele in doc.childNodes:
    if ele.nodeName=="Student":
        print("....Node:{0}.....".format(ele.nodeName))
        if ele.hasAttribute("desc"):
            print("Student-desc:{0}.....".format(ele.getAttribute("desc")))
        childs=ele.childNodes
        for child in childs:
            if child.nodeName=="Name":
                print("....Name:{0}.....".format(child.childNodes[0].data))
            if child.nodeName=="age":
                print("....Age:{0}.....".format(child.childNodes[0].data))
            if child.nodeName=="score":
                print("....Score:{0}.....".format(child.childNodes[0].data))
