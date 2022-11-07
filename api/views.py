from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
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


@method_decorator(csrf_exempt, name='dispatch')
class CalculationView(View):
    def post(self, request):
        if len(request.body) > 0 :
            json_data = json.loads(request.body)
            operation = json_data['operation_type']
            print(request.body)
            formatted_operation = operation.lower()
            x = json_data['x']
            y = json_data['y']
            
            
            if formatted_operation == 'multiplication':
               
                return JsonResponse(result, safe=False)
            elif formatted_operation =='addition':
                result = {
                "slackUsername": "solomonuche42",
                "operation_type": formatted_operation,
                "result": x + y,
            }
                return JsonResponse(result, safe=False)
            elif formatted_operation == 'subtraction':
                result = {
                "slackUsername": "solomonuche42",
                "operation_type": formatted_operation,
                "result": x - y,
            }
                return JsonResponse(result)
            else:
                return JsonResponse('Invalid operator', safe=False)
        return JsonResponse('No data posted. Please post  JSON DAT.', safe=False)