from django import forms


class CartAddProductForm(forms.Form):

    def __init__(self, max_quantity=20, *args, **kwargs):
        super().__init__(*args, **kwargs)
        PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, max_quantity+1)]
        self.fields['quantity'].choices = PRODUCT_QUANTITY_CHOICES

    quantity = forms.TypedChoiceField(
        coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
