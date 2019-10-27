from django import forms
from tapp.models import Product,Wishlist

#create your forms here:

class ProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = '__all__'

class WishlistForm(forms.ModelForm):
    class Meta():
        model = Wishlist
        fields = '__all__'