from django.forms import ModelForm, Textarea

from .models import ShopRequest


class ShopRequestFrom(ModelForm):
    class Meta:
        comment_palceholder = (
            'Можете, добавить ссылку на vk или '
            'whatsap тогда мы свяжимся с вами через них.'
        )
        model = ShopRequest
        exclude = ['is_delivered', 'card_id']
        widgets = {
            'address': Textarea(attrs={'cols': 'auto', 'rows': 1}),
            'comment': Textarea(attrs={
                'cols': 'auto', 'rows': 5, 'placeholder': comment_palceholder
                }
            )
        }
