from django.views.generic import View
from django.http import JsonResponse
# Create your views here.


class AboutView(View):
    def get(self, request):
        about_info = {
            "slackUsername": "solomonuche42",
            "backend": True,
            "age": 23,
            "bio": "I am detailed oriented.,,"
        }
        return JsonResponse(about_info)
