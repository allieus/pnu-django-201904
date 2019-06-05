from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet


class JSONEncoer(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return tuple(o)
        elif hasattr(o, 'as_dict'):
            return o.as_dict()
        
        return super().default(o)
