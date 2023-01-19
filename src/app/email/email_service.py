from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from jinja2 import Environment, select_autoescape, PackageLoader

from src.app.config.app import settings
from src.domain.account.user import User

env = Environment(
    loader=PackageLoader('src.app.email', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

class EmailService:
    def __init__(self, user: User, url: str, email: list[EmailStr]):
        self.name = f"{user.last_name} {user.first_name}"
        self.sender = 'Codevo <cd-admin@connecting-dots.com>'
        self.email = email
        self.url = url
        pass

    async def sendMail(self, subject, template):
        conf = ConnectionConfig(
            MAIL_USERNAME=settings.MAIL_USERNAME,
            MAIL_PASSWORD=settings.MAIL_PASSWORD,
            MAIL_FROM=settings.MAIL_FROM_ADDRESS,
            MAIL_PORT=settings.MAIL_PORT,
            MAIL_SERVER=settings.MAIL_HOST,
            MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
            MAIL_STARTTLS=False,
            MAIL_SSL_TLS=False,
            USE_CREDENTIALS=False,
            VALIDATE_CERTS=False
        )
        # Generate the HTML template base on the template name
        template = env.get_template(f'{template}.html')

        html = template.render(
            url=self.url,
            first_name=self.name,
            subject=subject
        )

        # Define the message options
        message = MessageSchema(
            subject=subject,
            recipients=self.email,
            body=html,
            subtype="html"
        )

        # Send the email
        fm = FastMail(conf)
        await fm.send_message(message)

    async def sendVerificationCode(self):
        await self.sendMail('Your verification code (Valid for 10min)', 'verification')