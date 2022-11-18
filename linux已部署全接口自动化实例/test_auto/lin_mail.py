import time
import yagmail



def lin_mail(a,time_ymd,time_hms):
    args = {
        "user": "ok.linliang@163.com",  # 发邮件账号
        "password": "ENNECDHQLNLGETKG",  # 发件账号对应的密码（QQ使用的是授权码，而不是QQ密码）
        "host": "smtp.163.com",  # 邮件账号的SMTP服务器
        "port": "465"  # SMTP服务器端口 465
    }
    # 收件人列表
    emailList = [
        "jing_910119@163.com",#自己
        "932860449@qq.com"
    ]
    email_attachments = [
        #附件添加
        ".//test_html//" + time_ymd + "//指挥中心全接口.html",
        #".//test_html//" + time_ymd + "//网页app全接口.html",
        ".//test_html//" + time_ymd + "//指挥中心接口操作流程.html",
        #".//test_html//" + time_ymd + "//网页app接口操作流程.html"
    ]
    email = yagmail.SMTP(**args)
    email.send(to=emailList, subject=time.strftime('%Y-%m-%d %X',time.localtime()), contents=a,attachments=email_attachments)
