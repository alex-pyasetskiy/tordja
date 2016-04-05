from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from polls_server import settings


class HelloAPI(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        return Response(dict(filter(lambda i: i if i[0].isupper() else None, settings.__dict__.iteritems())), status=status.HTTP_200_OK)