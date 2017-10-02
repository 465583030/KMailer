# KMailer Document

####Info:
#####author: Asahi Kuang
#####E-mail: asahikuang@gmail.com
#####date: 2017-10-02

--

#####Intro:
######Kmailer 服务器自发邮件程序，目前支持Gmail、QQ Mail.


#####Files:

- **kmailer_conf.py:** 配置SMTP类型，邮件发送地址和名字等

```
# SMTP服务器种类 eg. qq or gmail
smtp_sign = 'qq'  # 1
# 邮件登录账户
email_from_addr = 'xxxxxxxxxx@qq.com'
# 邮件登录密码
email_from_passwd = 'xxxxxxxxxx'
# 邮件发送地址，如有多个地址，使用","分隔
email_to_addr = 'xxxxxx@qq.com,xxxx@gmail.com'
# 邮件头显示的收件人姓名
email_to_name = 'XXX'
# 邮件头显示的发送人姓名
email_from_name = '大数据管理中心'
# 邮件附件日志文件显示名称
log_file_display_name = 'test.log'
```

- **kmailer_main.py:** main文件

- **kmailer_sender.py:** 邮件发送行为处理

```
def send_mail(self, from_name, to_name, to_addr, subject, content, file=None)

@param from_name: 邮件发送者显示名称
@param to_name: 邮件接收者显示名称
@param to_addr: 邮件接收邮箱地址
@param subject: 邮件显示主题
@param content: 邮件正文（文本）
@param file: 邮件附件（当前是文本文件 eg. ./Desktop/xxx.log）
```

- **kmailer_smtp_servers.py:** 配置一些可用的SMTP服务器和对应端口

- **kmailer_smtp_valid.py:** 配置SMTP服务器对应正确的端口信息（目前只配置了Gmail和QQ mail）

--

#####Usage:
######详见：`kmailer_main.py`文件
```
KMailerSender(smtp_sign, email_from_addr, email_from_passwd
                  ).send_mail(email_from_name, email_to_name, email_to_addr,
                              '北斗星车联大数据系统issue.',
                              'XCLBD Server Project Got Some Errors.Deal With It, please. (๑•ᴗ•๑)',
                              '/Users/asahi/Desktop/BDXC_BD.log')
```

--





