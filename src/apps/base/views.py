from rest_framework import views
from rest_framework import generics
from rest_framework import viewsets



class CustomAPIView(views.APIView):
    pass


class CustomGenericAPIView(generics.GenericAPIView):
    pass


class CustomListAPIView(generics.ListAPIView):
    pass


class CustomCreateAPIView(generics.CreateAPIView):
    pass


class CustomRetrieveAPIView(generics.RetrieveAPIView):
    pass


class CustomUpdateAPIView(generics.UpdateAPIView):
    pass


class CustomDestroyAPIView(generics.DestroyAPIView):
    pass


class CustomListCreateAPIView(generics.ListCreateAPIView):
    pass


class CustomRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    pass


class CustomRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    pass


class CustomRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    pass


class CustomViewSet(viewsets.ViewSet):
    pass


class CustomGenericViewSet(viewsets.GenericViewSet):
    pass


class CustomModelViewSet(viewsets.ModelViewSet):
    pass

class CustomReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    pass