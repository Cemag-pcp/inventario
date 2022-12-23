from paginas.models import tb_balanco
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = tb_balanco
        fields = ['codigo', 'familia']