from lxml import etree

html = etree.parse('structure03.xml')

print(type(html))

rst = html.xpath('//Student')
print(type(rst))
print(rst)

rst = html.xpath('//Student[@desc="PythonStudent"]')
print(type(rst))
print(rst)

rst = html.xpath('//Student[@desc="PythonStudent"]/name')
rst = rst [0]
print(type(rst))
print(rst)
print(rst.tag)
print(rst.text)