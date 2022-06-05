from turtle import position
from django_elasticsearch_dsl import ( 
    Document, fields, Index
)
from .models import booking

PUBLISHER_INDEX=Index('booking1')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):
    id=fields.IntegerField(attr="id")
    Image=fields.IntegerField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Lien=fields.TextField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Ville=fields.TextField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Localisation=fields.TextField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Position=fields.TextField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Etoile_Avis=fields.IntegerField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Avis=fields.TextField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Nbr_Experience=fields.TextField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Type_Chambre=fields.TextField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Type_Lit=fields.TextField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Duree=fields.IntegerField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Prix=fields.TextField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Taxes=fields.TextField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    Periode=fields.TextField(
        fields={
            "raw": {
                "type": 'keyword'
            }
        }
    )
    class Django(object):
        model=booking