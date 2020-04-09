import os
from PIL import Image
from removebg import RemoveBg


class ChangePic():
    def __init__(self,key,pic):
        self.key = key
        self.pic = pic

    def remove(self):
        """
        单张图片抠图
        :return:
        """
        rmove = RemoveBg(self.key,'error.log')
        path = os.getcwd()+'\\'+self.pic
        print(path)
        rmove.remove_background_from_img_file(path)


def changeBack(self,color):
    """
    更换背景色
    :param color:
    :return:
    """
    color_dict = {"A":(255,0,0),"B":(67,142,219),"C":(255,255,255)}
    img = self.pic+'_no_bg.png'
    im = Image.open(img)
    x,y = im.size
    try:
        p = Image.new('RGBA',im.size,color =color_dict.get(color))
        p.paste(im,(0,0,x,y),im)
        p.save('{}.png'.format('new'+color))

    except:
        print('change err')


ChangePic()