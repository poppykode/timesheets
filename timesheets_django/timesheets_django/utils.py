import random
import string
import datetime
from django.core.mail import EmailMessage
from accounts.models import User

def generate_employee_id(size=3, chars=string.ascii_uppercase + string.digits):
    the_id = "".join(random.choice(chars) for x in range(size))
    year  = str(datetime.date.today().year)
    employee_id = 'TDS' + year + the_id
    try:
        User.objects.get(username=employee_id)
        generate_employee_id()
    except:
        return employee_id

def generate_password():
    generated_pass = User.objects.make_random_password()
    return generated_pass

def send_password_and_username(username, email, password):
    print('send_password_and_username')
    try:
        subject = 'Account Creation for Timesheets'
        recipient_list = [email, ]
        email_body = """\
        <html>
        <head> </head>
        <body>
            <h2>New Account Details</h2>
            <p>URL: N/A</p>
            <p>Username: %s</p>
            <p>Password: %s</p>
        </body>
        </html>
        """ % (username, password,)
        mail = EmailMessage(
            subject,
            email_body,
            'TDS',
            recipient_list,
        )
        mail.content_subtype = "html"
        mail.send()
    except Exception as e:
        print(e)
