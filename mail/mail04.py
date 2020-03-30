from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase,MIMEMultipart
from email.header import Header
import smtplib

msg=MIMEText("Hey girl,do you have a date? ","plain","utf-8")

header_from=Header("从<1083138609@qqcom>发出去","utf-8")
msg['From']=header_from

# 填写接受者信息
header_to=Header("<1083138609@qqcom>接收信息","utf-8")
msg['To']=header_to

header_to=Header("mail主题","utf-8")
msg['Subject']=header_to

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
    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print(e)

