from lxml import etree

parser = etree.HTMLParser(encoding="utf-8")
html = etree.parse("lxml01.html", parser=parser)

rst = etree.tostring(html, pretty_print=True)
print(rst)

