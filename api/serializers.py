from rest_framework import serializers
from api.models import Company,Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"



class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    # company=serializers.ReadOnlyField()
    company = serializers.CharField(source='company.name')
    
    class Meta:
        model=Employee
        fields="__all__"
        


