from django.contrib import admin
from INV.forms import PartForm, AdminForm

# Register your models here.

from .models import Product,  Part, BOMS
class AdminProduct(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'Product_code', 'description',  'price', 'active','slug', 'image','Instructions1','Instructions2',  'Quantiti')
    search_fields = [ 'name', 'Product_code', 'description',  'price','slug', 'Quantiti']
    filter_horizontal = ['Part', 'BOMS']
    filter_vertical = ['Part']
    class Meta:
        model = Product

admin.site.register(Product, AdminProduct)






class AdminPart(admin.ModelAdmin):
    # list_filter = [ 'name', 'description', 'image', 'price','slug' ]
    list_display = ('__str__', 'name', 'PartNumber', 'description', 'image', 'price', 'active','slug', 'image', 'Quantiti' )
    search_fields = [ 'name', 'PartNumber', 'description', 'image', 'price','slug', 'Quantiti' ]
    list_editable = ('name', 'PartNumber', 'image', 'price','slug', 'Quantiti')
    # filter_vertical = [ 'name', 'PartNumber', 'description', 'image', 'price','slug', 'Quantiti' ]
    class Meta:
        model = Part

admin.site.register(Part, AdminPart)



class AdminBOM(admin.ModelAdmin):
    # list_filter = [ 'name', 'description', 'image', 'price','slug' ]
    list_display = ('__str__', 'name', 'PartNumber', 'description', 'Quantiti' )
    search_fields = [ 'name', 'PartNumber', 'description', 'Quantiti' ]
    list_editable = ('name', 'PartNumber', 'Quantiti')

    # filter_vertical = [ 'name', 'PartNumber', 'description', 'image', 'price','slug', 'Quantiti' ]
    class Meta:
        model = BOMS

admin.site.register(BOMS, AdminBOM)

# class PartFormAdmin(admin.ModelAdmin):
#     add_form = PartForm
#     fieldsets = (
#         'name', 'PartNumber', 'description', 'image', 'price', 'slug', 'Quantiti'
#
#     )
# admin.site.register(Part, PartFormAdmin)

# class EntryAdmin(admin.ModelAdmin):
#     add_form = AdminForm
#     fieldsets = (
#         ('Category', {
#             'fields': 'category'}),
#         ('Question', {'fields': ('question', 'q_active')}),
#         ('Answer Option', {'fields': ('option', 'option_active')}),
#         ('Selected Answer', {'fields': ('user_role', 'answer')}),
#     )
# admin.site.register( EntryAdmin)
#
#



















