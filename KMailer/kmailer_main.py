# -*- coding: utf8 -*-

__author__ = 'Asahi Kuang'

"""
    Main script to start KMailer sending mail via SMTP.
"""
from kmailer_sender import KMailerSender
from kmailer_conf import (email_from_addr, smtp_sign, email_from_passwd,
                          email_to_addr, email_from_name, email_to_name)


def main():
    KMailerSender(smtp_sign, email_from_addr, email_from_passwd
                  ).send_mail(email_from_name, email_to_name, email_to_addr,
                              '北斗星车联大数据系统issue.',
                              'XCLBD Server Project Got Some Errors.Deal With It, please. (๑•ᴗ•๑)',
                              '/Users/asahi/Desktop/BDXC_BD.log')


if __name__ == '__main__':
    main()
