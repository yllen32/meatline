from django.forms import ModelForm, Textarea

from .models import ShopRequest


class ShopRequestFrom(ModelForm):
    class Meta:
        model = ShopRequest
        exclude = ['is_delivered', 'card_id']
        widgets = {
            'address': Textarea(attrs={'cols': 40, 'rows': 1}),
            'comment': Textarea(attrs={'cols': 40, 'rows': 1})
        }
