from paginas.models import tb_balanco
import django_filters

class UserFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(field_name = 'codigo', lookup_expr='contains')

    class Meta:
        model = tb_balanco
        fields = ['codigo', 'familia']