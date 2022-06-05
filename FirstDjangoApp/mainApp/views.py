

import imp
from django.shortcuts import render
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from mainApp.documents import NewsDocument
from mainApp.serializers import NewsDocumentSerializer
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from .documents import *
from .serializers import *

# Create your views here.
class PublisherDocumentView(DocumentViewSet):
    document=NewsDocument
    serializer_class=NewsDocumentSerializer

    fiilter_backends=[
        FilteringFilterBackend,
        CompoundSearchFilterBackend
    ]

search_fields =('Image','Lien','Ville','Localisation','Position','Etoile_Avis','Avis','Nbr_Experience','Type_Chambre','Type_Lit','Duree','Prix','Taxes','Periode')
multi_match_search_fields=('Image','Lien','Ville','Localisation','Position','Etoile_Avis','Avis','Nbr_Experience','Type_Chambre','Type_Lit','Duree','Prix','Taxes','Periode')

fields_fields ={
    'Image':'Image',
    'Lien':'Lien',
    'Ville':'Ville',
    'Localisation':'Localisation',
    'Position':'Position',
    'Etoile_Avis':'Etoile_Avis',
    'Avis':'Avis',
    'Nbr_Experience':'Nbr_Experience',
    'Type_Chambre':'Type_Chambre',
    'Type_Lit':'Type_Lit',
    'Duree':'Duree',
    'Prix':'Prix',
    'Taxes':'Taxes',
    'Periode':'Periode'

}