import os, copy
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class Email_content:
    def __init__(self, subject, image_file, cid_name, template, template_params):
        assert isinstance(template, Template)
        assert isinstance(template_params, dict)
        self.msg = MIMEMultipart()

        self.msg['Subject'] = subject

        content = template.safe_substitute(**template_params)
        mime_content = MIMEText(content, 'html')
        self.msg.attach(mime_content)

        if image_file:
            assert template.template.find('cid:' + cid_name) >= 0
            assert os.path.isfile(image_file)
            with open(image_file, 'rb') as file:
                img = MIMEImage(file.read())
                img.add_header('Content-ID', '<' + cid_name + '>')
            self.msg.attach(img)

    def get_message(self, email_from, email_to):
        msg = copy.deepcopy(self.msg)
        msg['From'] = email_from  # from
        msg['To'] = ",".join(email_to)  # to
        return msg


class Email_sender:
    def __init__(self, host='smtp.gmail.com', port=587):
        self.host = host
        self.port = port
        self.server = smtplib.SMTP(host=host, port=port)
        self.server.starttls()
        self.server.login('email', 'password')  # email / password

    def send_message(self, email_content, email_from, email_to):
        content = email_content.get_message(email_from, email_to)
        self.server.send_message(content, from_addr=email_from, to_addrs=email_to)
        del content


class Inform:
    def send(self, image_file_name, name, time):
        host = 'smtp.gmail.com'
        port = 587
        send = Email_sender(host, port)

        subject = name
        template = Template("""<html>
                                    <head>Found it !!</head>
                                    <body>
                                        <img src='cid:inform'><br>
                                        This is a photo of ${NAME} at ${TIME}.<br>
                                    </body>
                                </html>""")
        template_params = {'NAME': name, 'TIME': time}
        image_file = image_file_name
        cid_name = 'inform'
        email_content = Email_content(subject, image_file, cid_name, template, template_params)

        email_from = 'from_email'
        email_to = ['to_email']
        send.send_message(email_content, email_from, email_to)
