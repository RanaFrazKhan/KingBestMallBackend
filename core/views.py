from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets,mixins,generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import *
from .serializer import *
import random
import string

# Create your views here.
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def check(request,):
    print(request.user)
    return Response(status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserProfile(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

class hhhh(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class ContactUs(viewsets.ViewSet):# class for contact us

    @action(detail=False, methods=['post'])
    def Post(self, request): #contact us post
        # user = request.data
        serializer = Contact_Us_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Thanks for contacting'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def Get_All(self, request):#get all contacts for admin
        user=request.user
        if UserProfile.objects.filter(role='A',user=user).exists():
            # print('if chl ria')
            recent_users = Contact_Us.objects.all().order_by('-id')

            # page = self.paginate_queryset(recent_users)
            # if page is not None:
            #     serializer = self.get_serializer(page, many=True)
            #     return self.get_paginated_response(serializer.data)

            serializer = Contact_Us_Serializer(recent_users, many=True)
            return Response(serializer.data)
        else:
            return Response({'status':'You are not admin'})
from django.template.loader import get_template
from django.core.mail.message import EmailMessage

def emailsending(key,template,email,msg):
    message = get_template(template).render(key)
    email = EmailMessage(msg, message, to=[email])
    email.content_subtype = 'html'
    email.send()
    print('Email Snd Successfully')

class User_Profile(viewsets.ViewSet):#User class

    @action(detail=False, methods=['post'])
    def SignUp(self, request):#function for signup
        if User.objects.filter(username=request.data['username']).exists():
            print(request.data['username'])
            return Response({"msg":"Already Registered"},status.HTTP_200_OK)
        else:
            user = User.objects.create_user(username=request.data['username'],
                                                email=request.data['email'],
                                                password=request.data['password'])
            if user !='':
                email=request.data['email']
                user = User.objects.get(email=email)
                secret_id = ''.join(
                    random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(200))
                key = {
                    'link': 'http://kingbestmall.com/verfiyemail/' + secret_id,
                    'username':request.data['username'],
                    # 'link': 'http://192.168.30.225:7000/VerfiyEmail/' + secret_id
                }
                profile_obj=request.data
                profile_obj.update({'user':user.id,'Activation_Key':secret_id})
                del profile_obj['username']
                del profile_obj['email']
                del profile_obj['password']
                serializer=ProfilePostSerializer(data=profile_obj)
                if serializer.is_valid():
                    serializer.save()
                    print('doneeeeeeeeee')
                    emailsending(key, 'Dhaar-Activation.html', email, 'Email Confirmation')
                    return Response({'Message': 'Successfully'}, status.HTTP_200_OK)
                else:
                    return Response({'error':serializer.errors})

            else:
                return Response({'Message':False}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def EmailConfirm(self,request):
        try:
            activition_key = request.data['activation_key']
            if (UserProfile.objects.filter(Activation_Key=activition_key).exists()):
                customer = UserProfile.objects.get(Activation_Key=activition_key)
                print('customer', customer)
                customer.ISConfirmed = True
                customer.save()
                return Response({'Message':'Account Activated'},status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


    @action(detail=False, methods=['post'])
    def IsActive(self,request):
        username = request.data['username']
        password=request.data['password']
        try:
            user = User.objects.get(username=username)
            success = user.check_password(password)

        except:
            return Response({'message': "Username does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if success is not False:
            user = User.objects.get(username=username)
            profile = UserProfile.objects.get(user=user.id)
            if profile.ISConfirmed == True:
                role=profile.role
                return Response({'Message': 'Account is Active', 'Role': role}, status=status.HTTP_200_OK)

            else:
                return Response({'Message': 'Account is Inactive'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message': 'Username or Password are wrong'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def GetEmail(self, request):
        try:
            username = request.user.username
            ProfileDeatils = User.objects.get(username=self.username).email
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            print(ProfileDeatils)
            return Response({'email': ProfileDeatils}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'],permission_classes=[IsAuthenticated])
    def ChangePassword(self,request):
        email1 = request.user.email
        currentPass=request.data['current']
        passN1=request.data['pass1']
        passN2=request.data['pass2']
        user = User.objects.get(email=email1)
        if user.check_password(currentPass) and passN1==passN2 and passN1!=currentPass:
            print('ok')
            user.set_password(passN1)
            user.save()
            key = {
                # 'link': 'https://www.rfpgurus.com/forgetpassword/' + reset_email_token
                'username': request.user.username,
                'password':passN1

            }
            # emailsending.after_response(key,'changepassword.html',email1,'Change Password')
            return Response({'msg':'PasswordChanged'},status=status.HTTP_200_OK)
        else:
            return Response({'msg':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def Username(self,request,User_pk=None):

        if User.objects.filter(username=User_pk).exists():
             return JsonResponse({'Res': True})
        else:
            return JsonResponse({'Res': False})

    @action(detail=False, methods=['get'])
    def Email(self,request,User_pk=None):

        if User.objects.filter(email=User_pk).exists():
             return JsonResponse({'Res': True})
        else:
            return JsonResponse({'Res': False})


class Password(viewsets.ViewSet):

    @action(detail=False, methods=['POST'])
    def Reset(self, request, User_pk=None):
        try:
            username = request.data['user']
            if User.objects.filter(Q(username=username) | Q(email=username)).exists():
                user = User.objects.get(Q(username=username) | Q(email=username))
                reg_obj = UserProfile.objects.get(user=user)
                if (reg_obj.ISConfirmed == True):
                    reset_email_token = ''.join(
                        random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _
                        in range(200))
                    while (UserProfile.objects.filter(Activation_Key=reset_email_token).exists()):
                        reset_email_token = ''.join(
                            random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
                            for _
                            in
                            range(100))
                    # key = {
                    #     'link': 'https://www.dhaar.pk/reset/' + str(user.id) + '/' + reset_email_token
                    # }
                    emailsending.after_response(key, 'password_reset_email.html', user.email, 'Password Reset')
                    reg_obj.Activation_Key = reset_email_token
                    reg_obj.save()
                    return Response({'message': 'Reset Password mail send Successfully'}, status.HTTP_200_OK)
                else:
                    return Response({'message': 'User Not verify'}, status.HTTP_200_OK)
            else:
                return Response({'message': 'Email Not Exist'}, status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['POST'])
    def ConfirmReset(request):
        try:
            activition_key = request.data['activation_key']
            password = request.data['password']
            if (UserProfile.objects.filter(Activation_Key=activition_key).exists()):
                customer = UserProfile.objects.get(Activation_Key=activition_key)
                print('customer', customer)
                user = User.objects.get(Q(username=customer) | Q(email=customer))
                user.set_password(password)
                user.save()
                return Response({'msg': 'Password Reset Successfully'}, status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['POST'])
    def user_confirmation(request):
        try:
            username = request.data['user']
            if User.objects.filter(Q(username=username) | Q(email=username)).exists():
                user = User.objects.get(Q(username=username) | Q(email=username))
                print('user', user)
                reg_obj = UserTableDB.objects.get(user=user)
                print('reg_obj ', reg_obj)
                if (reg_obj.ISConfirmed == False):
                    reset_email_token = ''.join(
                        random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
                        for _
                        in range(200))
                    while (UserTableDB.objects.filter(Activation_Key=reset_email_token).exists()):
                        reset_email_token = ''.join(
                            random.SystemRandom().choice(
                                string.ascii_uppercase + string.digits + string.ascii_lowercase)
                            for _
                            in
                            range(100))
                    print('reset_email_token', reset_email_token)
                    print(user.email)
                # key = {
                #     # 'link': 'https://www.rfpgurus.com/forgetpassword/' + reset_email_token
                #     'link': 'https://www.dhaar.pk/VerfiyEmail/' + reset_email_token,
                #     'user': user.username
                # }
                emailsending.after_response(key, 'signup_confirmation_email.html', user.email, 'Email Confirmation')
                reg_obj.Activation_Key = reset_email_token
                reg_obj.save()
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_202_ACCEPTED)


class Profile(mixins.RetrieveModelMixin, #mixins for each user profile
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes=[IsAuthenticated]
    def get(self, request, *args, **kwargs):#get profile
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):#update profile
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):#delete profile
        return self.destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class Subscribe(mixins.RetrieveModelMixin, #mixins for each user profile
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes=[IsAuthenticated]
    def get(self, request, *args, **kwargs):#get profile
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):#update profile
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):#delete profile
        return self.destroy(request, *args, **kwargs)