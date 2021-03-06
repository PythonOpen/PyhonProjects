from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase,MIMEMultipart
import smtplib

mail_mul=MIMEMultipart("alternative")

main_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <h1>这是一封HTML格式邮件</h1>

        </body>
        </html>
        """
msg=MIMEText(main_content,"html","utf-8")
mail_mul.attach(msg)

mail_text=MIMEText("Hey girl,do you have a date? ","plain","utf-8")
mail_mul.attach(mail_text)

# 发送email地址，此处地址直接使用个人QQ，密码一般需要临时输入，此处偷懒
from_addr="1083138609@qq.com"
# 此处密码是经过申请设置后的授权码，不是不是不是你的qq邮箱密码
from_pwd="ofgxddnrkxkqbaaf"

# 收件人信息
# 此处使用qq邮箱，我给我自己发送
to_addr="1083138609@qq.com"

# 输入SMTP服务器地址
# 此处根据不同的邮件服务商有不同的值
# 现在基本任何一家邮件服务商，如果采用第三方收发邮件，都需要开启授权选项
# 腾讯qq邮箱的smtp地址是 smtp.qq.com

smtp_srv="smtp.qq.com"

try:
    # 两个参数
    # 第一个是服务器地址，但一定是bytes格式，所以需要编码
    # 第二个参数是服务器的接受访问端
    # SMTP协议默认端口
    srv= smtplib.SMTP_SSL(smtp_srv.encode(), 25)
    # 登录邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件
    # 三个参数
    # 1.发送地址
    # 2. 接收地址，必须是list形式
    # 3.发送内容，作为字符串发送
    srv.sendmail(from_addr,[to_addr],mail_mul.as_string())
    srv.quit()
except Exception as e:
    print(e)

