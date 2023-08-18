from rest_framework.views import APIView, Response
from drf_yasg.utils import swagger_auto_schema
import generic.swagger_example as swg
from general.general import *

from account.models import Gender
from account.serializers import GenderSerializer



class GenderView(APIView):

    def get(self, request):
        gender = Gender.objects.all()
        serializer = GenderSerializer(gender, many=True)
        return Response(convert_response(serializer.data, 200))