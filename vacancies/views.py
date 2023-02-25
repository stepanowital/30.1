from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from vacancies.models import Vacancy


def hello(request):
	return HttpResponse("Hello World")


def index(request):
	if request.method == "GET":
		vacancies = Vacancy.objects.all()
		search_text = request.GET.get("text", None)
		if search_text:
			vacancies = vacancies.filter(text=search_text)

		response = []
		for vacancy in vacancies:
			response.append({
				"id": vacancy.id,
				"text": vacancy.text
			})

		return JsonResponse(response, safe=False)
		# return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


def get(request, vacancy_id):
	if request.method == "GET":
		try:
			vacancy = Vacancy.objects.get(pk=vacancy_id)
		except Vacancy.DoesNotExist:
			return JsonResponse(
				{"error": "Not Found"}, status=404
			)
		return JsonResponse({
			"id": vacancy.id,
			"text": vacancy.text
		})















