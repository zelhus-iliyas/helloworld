# from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import NoteSerializer
from .models import Notes


class NotesDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class NotesListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NotesCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NotesUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
