from rest_framework.views import APIView
from rest_framework import response
from rest_framework.permissions import AllowAny

from API.serializers import SumSerializer


class SumIntegers(APIView):
  permission_classes = [AllowAny]

  def post(self,request):
    print(request.data)
    # num1= request.data.get(num1)
    serialized = SumSerializer(data=request.data)
    isValid = serialized.is_valid(raise_exception=True)
    print(serialized.data)
    num1=serialized.data.get('num1')
    num2=serialized.data.get('num2')
    return response.Response({'sum':num1+num2})
