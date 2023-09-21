from rest_framework.views import APIView
from django.http import HttpResponse
from .models import *
from authUser.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken
import json


class help(APIView) :
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        access_token_str = str(request.auth)
        access_token_obj = AccessToken(access_token_str)
        requesting_agency = CustomUser.objects.get(id=access_token_obj['user_id'])
        requesting_agency_ID = requesting_agency.agencyID
        requesting_agency_name = requesting_agency.agencyName
        requesting_agency_latitude = requesting_agency.latitude
        requesting_agency_longitude = requesting_agency.longitude


        message = "Agency: " + requesting_agency_name + " whose current location is: " + str(requesting_agency_latitude) + " latitude and " + str(requesting_agency_longitude) + " longitude needs your help"

        all_other_agencise = CustomUser.objects.all()

        try:
            for i in all_other_agencise:
                if(i.agencyID != requesting_agency_ID and i.agencyID != 'admin'):
                    new_notification = agencyNotification.objects.create(agency = i)
                    new_notification.notifications = message
                    new_notification.save()
            RESPONSE = "success"
            STATUS = 200
        
        except:

            RESPONSE = "server error"
            STATUS = 400
            
        return HttpResponse(RESPONSE, status = STATUS)


class getNotifications(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        access_token_str = str(request.auth)
        access_token_obj = AccessToken(access_token_str)
        agency = CustomUser.objects.get(id=access_token_obj['user_id'])

        try:

            agency_notifications = agencyNotification.objects.filter(agency=agency).last()

            if(agency_notifications):
                RESPONSE = json.dumps({"notifications": agency_notifications.notifications})
                STATUS = 200

            else:
                RESPONSE = "no new notification"
                STATUS = 204

        except:

            RESPONSE = "server error"
            STATUS = 400

        return HttpResponse(RESPONSE, status=STATUS)

        