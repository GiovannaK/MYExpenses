from .models import *


class CurrencyCreationObjectMixin:
    model = None 
    form_class = None 
    template_name = None 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        validate_create_currency = Currencies.objects.all().exists()
        if validate_create_currency == False:
            with open(os.path.join(settings.BASE_DIR, 'currency.json'), 'r', 
            encoding="utf8") as data:
                data_json = json.loads(data.read())
                for v in data_json.values():
                    symbol = v["symbol"]
                    create_currency = Currencies.objects.create(currency=symbol)
        get_currency = Currencies.objects.all()
        context["currencies"] = get_currency
        return context 
    