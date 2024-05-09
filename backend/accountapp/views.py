from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vote
from .serializers import VoteSerializer

class PostAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            if (serializer.validated_data['vote'] == 'biden'):
                vote = Vote.objects.first()
                vote.biden_count += 1
                vote.save()
                Response(status=status.HTTP_201_CREATED)
            elif (serializer.validated_data['vote'] == 'trump'):
                vote = Vote.objects.first()
                vote.trump_count += 1
                vote.save()
                Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class GetAPI(APIView):
    def get(self, request, *args, **kwargs):
        vote = Vote.objects.first()
        return Response({'biden_count': vote.biden_count, 'trump_count': vote.trump_count})

