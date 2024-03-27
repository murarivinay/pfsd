import csv

from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def success1(request):
    return render(request,'successfullysentmail.html')


def send_email1(request):
    csv_file_path =r'E:\Python\DjangoProject\TTM\static\mail.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here
            send_mail(
                subject,
                message_body,
                '2200032512cseh@gmail.com',
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
            messages.info(request, 'Email Sent Successfully Sented.')
    return render(request, 'successfullysentmail.html')