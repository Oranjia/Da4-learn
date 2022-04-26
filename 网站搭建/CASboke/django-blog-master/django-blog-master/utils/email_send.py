import random
import string
from datetime import datetime
from users.models import EmailVerifyRecord
from django.core.mail import send_mail



def random_str(randomlength=8):
    """ 生成8位数的随机字符串方法 """
    chars = string.ascii_letters + string.digits   # 生成a-zA-Z0-9字符串
    strcode = ''.join(random.sample(chars, randomlength))  # 生成随机的8位数字符串
    return strcode


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    # email_record.add_time = datetime.now()
    email_record.save()
    
    if send_type == 'register':
        email_title = '博客的注册激活链接'
        email_body = '请点击以下链接激活账号：http://127.0.0.1:8000/users/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, 'oranjia@vip.qq.com', [email])
        if send_status:
            pass
    
    elif send_type == 'forget':
        email_title = '找回密码链接'
        email_body = '请点击以下链接修改密码：http://127.0.0.1:8000/users/forget_pwd_url/{0}'.format(code)

        send_status = send_mail(email_title, email_body, 'oranjia@vip.qq.com', [email])
        if send_status:
            pass