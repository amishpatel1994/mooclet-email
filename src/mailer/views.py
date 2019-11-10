from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
# Create your views here.

@api_view(['POST'])
def send_email(request):
	body = request.data
	sender_email = "Amish Patel <av2patel94@gmail.com>"
	#TODO: Make the API call to MOOClet here to get email content for the email recepients
	email_recepients = body["emails"]
	dummy_subject = "It works!"
	dummy_content = "This will get sent through Mailgun"
	for email in email_recepients:
		send_mail(dummy_subject, dummy_content, sender_email, [email])

	return Response(status=200, data="Emails sent.")

@api_view(['POST'])
def new_email_metric(request):
	#TODO: Make the API call to MOOClet to send email metrics back to MOOClet
	return Response(status=200, data="Got new metric")