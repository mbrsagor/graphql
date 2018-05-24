from django import forms
from django.forms import TextInput, Textarea, Select, RadioSelect, DateInput
from .models import Product, Slider, Category, Color, Brand



# Contact Form
class Contact_Forms(forms.Form):
    name = forms.CharField(required = True,  widget=forms.TextInput(attrs={'class': 'form-control input'}))
    email = forms.EmailField(required = True,  widget=forms.TextInput(attrs={'class': 'form-control input'}))
    message = forms.CharField(required = True,  widget=forms.Textarea(attrs={'class': 'form-control textarea'}))



# Add New Product
class AddNewProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')

        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'category' : Select(attrs={'class':'select'}),
            'color' : Select(attrs={'class':'select'}),
            'discount_price' : TextInput(attrs={'class':'form-control'}),
            'discount_off_price' : TextInput(attrs={'class':'form-control'}),
            'price' : TextInput(attrs={'class':'form-control'}),
            'product_code' : TextInput(attrs={'class':'form-control'}),
            'brand_name' : Select(attrs={'class':'form-control'}),
            'order_now_link' : TextInput(attrs={'class':'form-control'}),
            'description' : Textarea(attrs={'class':'form-control'}),
        }



# Add New Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')
        widgets = {
            'name' : TextInput(attrs={'class': 'form-control'})
        }



# Edit Product Item
class Slider_Form(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ('__all__')



# Adding Color
class AddingColor_Form(forms.ModelForm):
    class Meta:
        model = Color
        fields = ('__all__')

        widgets = {
            'name' : TextInput(attrs={'class': 'form-control'})
        }


# Adding Brand
class AddingBrand_Form(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('__all__')

        widgets = {
            'name' : TextInput(attrs={'class': 'form-control'})
        }



# Product Comment/review
class ProductComment_Form():
    pass