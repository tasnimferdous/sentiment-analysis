from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from sentiment.models import Sentence
from sentiment.api.serializers import SentenceSerializer
from sentiment.pretrained_models import *


class SentenceView(APIView):
    """ Api to get a response on analyzed text."""

    def get(self, request):
        sentence = Sentence.objects.all()
        serializer = SentenceSerializer(sentence, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SentenceSerializer(data = request.data)
        if serializer.is_valid():
            # serializer.save()
            #any one of the following
            # sentiment = sentiment_textblob(serializer.data['text'])
            sentiment = sentiment_vader(serializer.data['text'])
            return Response({"sentiment":sentiment}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)