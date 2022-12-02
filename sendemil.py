from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
from email.mime.image import MIMEImage
def send(TET):
    mail_host = "smtp.163.com" #SMTP服务器地址
    mail_sender = "micaiabc@163.com" #账号
    mail_passwd = "OLDOJFMMIZDIEQFE" #密码

    msg = MIMEMultipart('related')
    msg["Subject"] = "学习强国"
    msg["From"] = mail_sender #发送人
    msg["To"] = "2544624953@qq.com" #接收人
    if TET == '':
        #html格式的邮件正文
        # html格式的邮件正文
        content = '''
        <body>
        <p>学习强国</p>
        <p>图片如下：</p>
        <p><img src="cid:testimage" alt="testimage"></p>
        </body>
        '''
        msg.attach(MIMEText(content, 'html', 'utf-8'))

        # 读取图片
        fp = open('photo.png', 'rb')  # 打开文件
        msgImage = MIMEImage(fp.read())  # 读入 msgImage 中
        fp.close()  # 关闭文件

        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', 'testimage')
        msg.attach(msgImage)

    else:
        msgtet = MIMEText(TET + time.strftime("%Y-%m-%d ", time.gmtime()), 'plain', 'utf-8')
        msg.attach(msgtet)
    ## 发送邮件
    s = smtplib.SMTP() #实例化对象
    s.connect(mail_host, 25) #连接163邮箱服务器，端口号为25
    s.login(mail_sender, mail_passwd) #登录邮箱
    s.sendmail(mail_sender, [msg["To"]], msg.as_string())
    s.quit()




