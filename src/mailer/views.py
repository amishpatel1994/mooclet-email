from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
import requests
import os
# Create your views here.

@api_view(['POST'])
def send_email(request):
	body = request.data
	sender_email = "FName LName <something@domain.com>"
	BASE_URL = "https://celery.mooclet.com/engine/api/v1/mooclet/"
	mooclet_id = body["id"]
	URL = BASE_URL + mooclet_id + "/run?user_id="
	email_recepients = body["emails"]

	for email in email_recepients:
		request_URL = URL+email
		mooclet_response = requests.get(request_URL, headers={'Authorization': os.getenv("MOOCLET_API_KEY")})
		email_subject = mooclet_response.json()["name"]
		email_body = mooclet_response.json()["text"]
		send_mail(email_subject, email_body, sender_email, [email])

	return Response(status=200, data="Emails successfully sent!")

@api_view(['POST'])
def new_email_metric(request):
	#TODO: Make the API call to MOOClet to send email metrics back to MOOClet
	return Response(status=200, data="Got new metric")
