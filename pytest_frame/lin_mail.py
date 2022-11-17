import time
import yagmail



def lin_mail(a,time_ymd,time_hms):
    args = {
        "user": "ok.linliang@163.com",  # 发邮件账号
        "password": "1991119",  # 发件账号对应的密码（QQ使用的是授权码，而不是QQ密码）
        "host": "smtp.163.com",  # 邮件账号的SMTP服务器
        "port": "465"  # SMTP服务器端口 465
    }
    # 收件人列表
    emailList = [
        "jing_910119@163.com"#自己
    ]
    email_attachments = [
        #附件添加
        "D://xxx//" + time_ymd + "/" + time_hms + "xxx.html"
    ]
    email = yagmail.SMTP(**args)
    email.send(to=emailList, subject=time.strftime('%Y-%m-%d %X',time.localtime()), contents=a,attachments=email_attachments)