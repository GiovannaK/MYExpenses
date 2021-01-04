from django.template import context
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from expenses.models import Expenses
from django.contrib.sites.models import Site

def send_expense_email():
    current_site = Site.objects.get_current().domain
    users_email_list = Expenses.objects.filter(long_term=True).values('author__user__email')
    users_email_results = [email["author__user__email"] for email in users_email_list.iterator()]
    context = {'current_site': current_site}
    subject = "MYExpenses | Despesas mensais"
    body = render_to_string('expenses_reminder_message.txt', context)

    email = EmailMessage(
        subject, 
        body, 
        settings.EMAIL_HOST_USER, 
        bcc=users_email_results,
    )

    return email.send(fail_silently=False)


