from .models import booking
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer    
from .documents import *

class NewsDocumentSerializer(DocumentSerializer):
    class Meta:
        model= booking
        document= NewsDocument

        fields=('classement', 'name', 'position', 'age', 'nationality', 'club', 'value', 'apt', 'goals', 'red_goals', 'assisted_goals', 'yellow_card', 'red_card')
        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}
