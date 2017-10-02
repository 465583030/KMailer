# -*- coding: utf8 -*-

__author__ = 'Asahi Kuang'

"""
    Some SMTP servers:
        - SMTP_GMAIL with number 1, alias gmail.
        - SMTP_QQ_MAIL mail with number 2, alias qq.
        - SMTP_YAHOO_MAIL mail with number 3, alias yahoo.
        - SMTP_163_MAIL mail with number 4, alias mail163
    .
"""

from enum import Enum
from kmailer_smtp_valid import smtp_server_and_port


# Every SMTP server get a number
class KMailerSMTPServerEnum(Enum):

    # gmail
    SMTP_GMAIL = 1
    gmail = 1

    # QQ mail
    SMTP_QQ_MAIL = 2
    qq = 2

    # Yahoo mail
    SMTP_YAHOO_MAIL = 3
    yahoo = 3

    # 163 mail
    SMTP_163_MAIL = 4
    mail163 = 4


class KMailerSMTPServer:

    def __init__(self, smtp_sign):
        KMailerSMTPServer.verify_sign(smtp_sign)
        try:
            self.server = KMailerSMTPServerEnum[smtp_sign] if isinstance(smtp_sign, str)\
                else KMailerSMTPServerEnum(smtp_sign)
        except ValueError as e:
            print(e)

    def get_smtp_server_and_port(self):
        return smtp_server_and_port[self.server.name]

    @staticmethod
    def verify_sign(sign):
        str_valid = ('SMTP_GMAIL', 'gmail', 'SMTP_QQ_MAIL', 'qq',
                     'SMTP_YAHOO_MAIL', 'yahoo', 'SMTP_163_MAIL', 'mail163')
        int_valid = (1, 2, 3, 4)
        if isinstance(sign, str) & (sign not in str_valid):
            raise Exception('The SMTP sign is not valid.')
        elif isinstance(sign, int) & (sign not in int_valid):
            raise Exception('The SMTP sign is not valid.')
        else:
            pass


if __name__ == '__main__':
    y = KMailerSMTPServer(2)
    y.get_smtp_server_and_port()
