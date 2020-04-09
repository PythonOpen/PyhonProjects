from PIL import Image
import os

i = 1
j = 1

dir_lists = ["images"]
dir_out_lists = ["LUCKY2"]
for i in range(0, 1):
    dir_in = dir_lists[i]
    dir_out = dir_out_lists[i]
    path = "E:/Working/PythonProjects/myPython/Exercise/"
    img_dir_root = os.path.join(path, dir_in)
    img_dir_out_root = os.path.join(path, dir_out)
    img_files = os.listdir(img_dir_root)
    img_files.sort(key=lambda x: int(x[0:-4]))
    img_files.reverse()
    count = 0
    for file_name in img_files:
        img_path = os.path.join(img_dir_root, file_name)
        img = Image.open(img_path)  # 读取系统的内照片
        width = img.size[0]  # 长度
        height = img.size[1]  # 宽度
        for i in range(0, width):  # 遍历所有长度的点
            for j in range(0, height):  # 遍历所有宽度的点
                data = (img.getpixel((i, j)))  # 打印该图片的所有点
                # print(data)  # 打印每个像素点的颜色RGBA的值(r,g,b,alpha)
                # print(data[0])  # 打印RGBA的r值
                if data[0] >= 200 and data[1] >= 200 and data[2] >= 200:  # RGBA的r值大于170，并且g值大于170,并且b值大于170
                    img.putpixel((i, j), (255, 255, 255, 255))  # 则这些像素点的颜色改成大红色
        img = img.convert("RGB")  # 把图片强制转成RGB
        img.save(img_dir_out_root + "/" + str(count) + ".jpg")  # 保存修改像素点后的图片
        count += 1

