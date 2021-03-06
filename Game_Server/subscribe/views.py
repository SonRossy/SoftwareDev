from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
import json
from subscribe.models import Subscribe
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import urllib.request

class HomePageView(APIView):
	@csrf_exempt
	def create_or_retrieve(self, request=None, uname="test", subl = 0,format=None):
		page = urllib.request.urlopen('http://localhost:8000/user/'+uname)
		json_string = page.read()
		parsed_json = json.loads(json_string)
		
		if request.method == "GET":
			try:
				found_id = parsed_json['id']
				user_id = Subscribe.objects.get(id = found_id)
			except ObjectDoesNotExist as e:
				return HttpResponse(json.dumps({"status":"NoSuchID"}),status = 404)
			
			data = {"id":user_id.id, "level":user_id.level}
			return HttpResponse(json.dumps(data),status = 200)
		
		elif request.method == "POST":
			try:
				found_id = parsed_json['id']
				user_id = Subscribe.objects.get(id = found_id)
				return HttpResponse(json.dumps({"status":"AlreadyExists"}),status=403)
			except ObjectDoesNotExist as e:
				pass
			u = Subscribe(id = found_id)
			u = Subscribe(level = subl)
			u.save()
			return HttpResponse(json.dumps({"status":"Success"}))
			
		elif request.method == "PUT":
			try:
				found_id = parsed_json['id']
				user = Subscribe.objects.get(id = found_id)
				user.level = subl
				user.save()
				return HttpResponse(json.dumps({"status":"Success"}))
			except ObjectDoesNotExist as e:
				return HttpResponse(json.dumps({"status":"NoSuchUser"}))