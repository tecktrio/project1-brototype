from django import forms

from shopping_app.models import all_products, banner, Company_Info


class add_product_form(forms.ModelForm):
    class Meta:
        model = all_products
        fields = ['product_name','product_description','product_image','product_mrp','product_price','product_category','product_sub_category','product_specification_1','product_specification_2','product_gender','product_stock_available','product_rating','product_total_sold','product_is_trusted','product_review_id','product_status']

class add_banner(forms.ModelForm):
    class Meta:
        model = banner
        fields = ['banner_name','banner_img']


class company_info(forms.ModelForm):
    class Meta:
        model = Company_Info
        fields = ['company_logo','company_name','company_description']