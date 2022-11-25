from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Movie
from .serializers import MovieSerializer

class GetMoviesView(ListAPIView):
    queryset = Movie.objects.all().order_by('releaseYear')
    serializer_class = MovieSerializer

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)