from .serializers import wordSerializers
from rest_framework import permissions, viewsets

class wordViewSet(viewsets.ModelViewSet):

    #setup permission
    permission_classes = [permissions.IsAuthenticated]

    #pick serializer
    serializer_class = wordSerializers

    #configure the queryset, user can only make query to their word objects
    def get_queryset(self):
        return self.request.user.word.all() #'word' here is the related_name for fk in word's model

    #configure the create for new word object
    def perform_create(self, serializer):

        #set the default value of attribute owner to user id
        serializer.save(owner=self.request.user)