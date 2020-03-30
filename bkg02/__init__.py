#如果有__all__则不会执行inInit()的内容
__all__=['p01']

def inInit():
    print("I am in init of package")