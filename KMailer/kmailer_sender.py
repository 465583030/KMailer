# -*- coding: utf8 -*-

__author__ = 'Asahi Kuang'

from kmailer_smtp_servers import KMailerSMTPServer
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.utils import parseaddr, formataddr
from email.header import Header
from kmailer_conf import log_file_display_name


class KMailerSender:

    def __init__(self, sign, from_addr, pwd):
        servers = KMailerSMTPServer(sign).get_smtp_server_and_port()
        self.smtp_server_addr = servers['smtp']
        self.smtp_port = servers['port']
        self.from_addr = from_addr
        self.pwd = pwd

    # 格式化地址
    @staticmethod
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def _make_server(self, to_addr, mime):
        # 处理多个接收邮件地址
        to_addrs = to_addr.split(',')

        server = smtplib.SMTP(self.smtp_server_addr, self.smtp_port)

        # 调试等级   > 0 输出日志  0 不输出
        server.set_debuglevel(1)
        server.starttls()
        server.login(self.from_addr, self.pwd)
        server.sendmail(self.from_addr, to_addrs, mime.as_string())
        server.close()

    def send_mail(self, from_name, to_name, to_addr, subject, content, file=None):
        mime = MIMEMultipart()
        mime['From'] = KMailerSender._format_addr(
            '{} <{}>'.format(from_name, self.from_addr))
        mime['To'] = KMailerSender._format_addr(
            '{} <{}>,{} <{}>'.format(to_name, to_addr, 'low', 'kqx165@live.com'))
        mime['Subject'] = Header(subject, 'utf-8').encode()
        mime.attach(MIMEText(content, 'plain', 'utf-8'))

        # 绑定附件
        KMailerSender._attach_log_file(mime, file)

        # 发送
        self._make_server(to_addr, mime)

    @staticmethod
    def _attach_log_file(mime, file):
        # 添加附件
        if file:
            with open(file, 'rb') as f:
                mime_base = MIMEBase('text', 'log', filename=log_file_display_name)
                # 加上必要的头信息:
                mime_base.add_header('Content-Disposition', 'attachment',
                                     filename=log_file_display_name)
                mime_base.add_header('Content-ID', '<0>')
                mime_base.add_header('X-Attachment-Id', '0')
                mime_base.set_payload(f.read())
                mime.attach(mime_base)


if __name__ == '__main__':
    pass
