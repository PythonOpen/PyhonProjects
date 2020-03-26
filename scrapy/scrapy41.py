import pytesseract as pt
from PIL import Image

image = Image.open(r'D:\我的文档\Desktop\未处理\591d6b2d03abb.jpeg')

# 调用pytesseract,把图片转换成文字
# 返回结果就是转换后的结果
text = pt.image_to_string(image)
print(text)
