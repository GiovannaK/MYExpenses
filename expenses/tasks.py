from __future__ import absolute_import, unicode_literals

from celery import shared_task

from .email import send_expense_email

@shared_task
def send_expense_email_task():
    return send_expense_email()
