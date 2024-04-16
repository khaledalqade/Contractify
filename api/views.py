from rest_framework import request, status, viewsets
#from .models import Meal, Rating
#from .serializers import MealSerializer, RatingSerializer, UserSerializer
from .serializers import UserSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.authtoken.models import Token


from rest_framework.viewsets import ModelViewSet
from .models import Contract
from .serializers import ContractSerializer



from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # #authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({
                'token': token.key, 
                }, 
            status=status.HTTP_201_CREATED)
    




class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    authentication_classes = (TokenAuthentication, )


    @action(detail=False, methods=['GET'])
    def contracts_false_approval(self, request):
        current_user = request.user
        contracts = self.queryset.filter(approval=False, 
                                         buyer_signature=False, 
                                         seller_id_number=current_user.username)
        serializer = self.serializer_class(contracts, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['GET'])
    def contracts_true_approval(self, request):
        current_user = request.user
        contracts = self.queryset.filter(approval=True, 
                                         buyer_signature=False, 
                                         seller_signature=False, 
                                         buyer_id_number=current_user.username)
        serializer = self.serializer_class(contracts, many=True)
        return Response(serializer.data)



    @action(detail=False, methods=['GET'])
    def approved_contracts_true_buyer(self, request):
        current_user = request.user
        contracts = self.queryset.filter(approval=True, 
                                         buyer_signature=True, 
                                         seller_signature=False, 
                                         seller_id_number=current_user.username)
        serializer = self.serializer_class(contracts, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def approved_contracts_true_buyer_ready(self, request):
        current_user = request.user
        contracts = self.queryset.filter(approval=True, 
                                         buyer_signature=True, 
                                         seller_signature=True, 
                                         buyer_id_number=current_user.username)
        serializer = self.serializer_class(contracts, many=True)
        return Response(serializer.data)
    
    
    @action(detail=False, methods=['GET'])
    def approved_contracts_true_seller_ready(self, request):
        current_user = request.user
        contracts = self.queryset.filter(approval=True, 
                                         buyer_signature=True, 
                                         seller_signature=True, 
                                         seller_id_number=current_user.username)
        serializer = self.serializer_class(contracts, many=True)
        return Response(serializer.data)
