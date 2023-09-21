from .models import *
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializers import *
import json


class preRegister(APIView):

    def post(self, request):
        data = request.data
        agencyName = data["agencyName"]
        password = data["password"]
        confirmPassword = data["confirmPassword"]
        agencyID = data["agencyID"]

        agency = CustomUser.objects.filter(agencyID = agencyID)

        if(len(agency)):
            RESPONSE = "agencyID already exists"
            STATUS = 400
        
        else:
            if(password != confirmPassword):
                RESPONSE = "confirm password and password should match"
                STATUS = 400
            
            else:
                agencyNew = CustomUser.objects.create(agencyName = agencyName, agencyID = agencyID, password = password)
                agencyNew.set_password(password)
                agencyNew.save()
                token = RefreshToken.for_user(agencyNew)
                RESPONSE = json.dumps({'status': "success", "refresh_token": str(token), "access_token": str(token.access_token)})
                STATUS = 200
        
        return HttpResponse(RESPONSE, status=STATUS)



class edit_Details(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        type = data['type']
        frequency = data['frequency']
        resources = data['resources']
        SOPs = data['spos']
        emergencyplan = data['emergencyplan']
        latitude = data["latitude"]
        longitude = data["longitude"]
        
        try:
            access_token_str = str(request.auth)
            access_token_obj = AccessToken(access_token_str)
            agency = CustomUser.objects.get(id=access_token_obj['user_id'])
            agency.type = type
            agency.frequency = frequency
            agency.resources = resources
            agency.SOPs = SOPs
            agency.emergencyplan = emergencyplan
            agency.latitude = latitude
            agency.longitude = longitude
            agency.save()

            RESPONSE = "success"
            STATUS = 200
        
        except:

            RESPONSE = "server error"
            STATUS = 400

        return HttpResponse(RESPONSE, status = STATUS)



class getDetails(APIView) :

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        access_token_str = str(request.auth)
        access_token_obj = AccessToken(access_token_str)
        agency_id = access_token_obj['user_id']
        agency = CustomUser.objects.get(id=agency_id)

        try:

            agencyName = agency.agencyName
            agencyID = agency.agencyID
            agencyType = agency.type
            frequency = agency.frequency
            resources = agency.resources
            SOPs = agency.SOPs
            emergencyPlan = agency.emergencyplan
            longitude = agency.longitude
            latitude = agency.latitude

            agencyDetails = json.dumps({'name': agencyName, 'ID': agencyID, 'type': agencyType, 'frequency': frequency, 'resource': resources, 'sops': SOPs, 'emergencyPlan': emergencyPlan, 'longitude': longitude, 'latitude': latitude})

            RESPONSE = agencyDetails
            STATUS = 200

        except:

            RESPONSE = "Error"
            STATUS = 400

        return HttpResponse(RESPONSE, status = STATUS)
    


class getAgenciesLocation(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        access_token_str = str(request.auth)
        access_token_obj = AccessToken(access_token_str)
        agency_id = access_token_obj['user_id']
        agency = CustomUser.objects.get(id=agency_id)

        try:
            other_agency_location_details = []
            agency_details = {'agencyID': agency.agencyID, 'agencyName': agency.agencyName, 'longitude': agency.longitude, 'latitude': agency.latitude}

            other_agency_location_details.append(agency_details)

            all_agency = CustomUser.objects.all()

            for i in all_agency:
                if(i.agencyID != agency.agencyID and i.agencyID != 'admin'):
                    agency_details = {'agencyID': i.agencyID, 'agencyName': i.agencyName, 'longitude': i.longitude, 'latitude': i.latitude}

                    other_agency_location_details.append(agency_details)

            RESPONSE = json.dumps(other_agency_location_details)
            STATUS = 200

        
        except:
            RESPONSE = "server error"
            STATUS = 400

        return HttpResponse(RESPONSE, status=STATUS)



