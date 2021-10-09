from rest_framework import serializers
from .models import DatabaseModel


# declare the database serializer for use with the django rest framework
class DatabaseSerializer(serializers.HyperlinkedModelSerializer):
    # here we define the database model to use
    class Meta:
        model = DatabaseModel
        # we explicitly define which columns we want to expose to the user via the REST endpoint
        fields = ('col_id', 'col_str', 'col_num', 'col_date')
