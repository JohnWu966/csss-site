# Register your models here.
from django.contrib import admin
from shopping.models import Order, Merchandise, Option, OptionChoice, SelectedOrderMerchandise, SelectedOrderMerchandiseOptionChoice, Customer
from django.utils.translation import ugettext_lazy as _
# Register your models here.


def create_default_choices(mailbox_admin, request, queryset):
	for merch in queryset.all():
		print(f"digesting {merch.merchandise}")
		opt1 = Option(
			option_merchandise_key = merch,
			option = 'Size'
		)
		opt1.save()
		ch1x1 = OptionChoice(
			optionChoice_option_key = opt1,
			choice = 'X-Small'
		)
		ch1x1.save()
		ch1x2 = OptionChoice(
			optionChoice_option_key = opt1,
			choice = 'Small'
		)
		ch1x2.save()
		ch1x3 = OptionChoice(
			optionChoice_option_key = opt1,
			choice = 'Medium'
		)
		ch1x3.save()
		ch1x4 = OptionChoice(
			optionChoice_option_key = opt1,
			choice = 'Large'
		)
		ch1x4.save()
		ch1x5 = OptionChoice(
			optionChoice_option_key = opt1,
			choice = 'X-Large'
		)
		ch1x5.save()
		ch1x6 = OptionChoice(
			optionChoice_option_key = opt1,
			choice = 'X-Large'
		)
		ch1x6.save()
		opt2 = Option(
			option_merchandise_key = merch,
			option = 'Color'
		)
		opt2.save()
		ch2x1 = OptionChoice(
			optionChoice_option_key = opt2,
			choice = 'Navy Blue'
		)
		ch2x1.save()
		ch2x2 = OptionChoice(
			optionChoice_option_key = opt2,
			choice = 'Black'
		)
		ch2x2.save()
		ch2x3 = OptionChoice(
			optionChoice_option_key = opt2,
			choice = 'Grey'
		)
		ch2x3.save()
		ch2x4 = OptionChoice(
			optionChoice_option_key = opt2,
			choice = 'Red'
		)
		ch2x4.save()

create_default_choices.short_description = _('Create Default Choices')

class CustomerAdmin(admin.ModelAdmin):
    list_display = (
    'name',
    'get_sfu_email'
    )
    def get_sfu_email(self, obj):
        return obj.sfu_email
    get_sfu_email.short_description = "SFU Email"
    get_sfu_email.admin_order_field = "sfu_email"

class OrderAdmin(admin.ModelAdmin):
    list_display = (
    'get_order_id',
    'get_customer_name',
    'date',
    'time'
    )
    def get_order_id(self, obj):
        return obj.order_id
    get_order_id.short_description = 'Order ID'
    get_order_id.admin_order_field = 'order_id'

    def get_customer_name(self, obj):
        return obj.order_customer_key.name
    get_customer_name.short_description = 'Customer Name'
    get_customer_name.admin_order_field = 'customer_name'

class MerchandiseAdmin(admin.ModelAdmin):
	list_display = (
	'id',
	'merchandise',
	'image',
    'price'
	)
	actions = [create_default_choices]

class OptionAdmin(admin.ModelAdmin):
	list_display = (
	'id',
	'option_merchandise_key',
	'option',
	)

class OptionChoiceAdmin(admin.ModelAdmin):
	list_display = (
	'id',
	'optionChoice_option_key',
	'choice',
	)

class SelectedOrderItemAdmin(admin.ModelAdmin):
    list_display = (
    'get_order_id',
    'get_order_merchandises'
    )
    def get_order_id(self, obj):
        return obj.orderItem_order_key.order_id
    get_order_id.short_description = 'Order ID'
    get_order_id.admin_order_field = 'order_id'

    def get_order_merchandises(self, obj):
        return obj.orderItem_merchandise_key.merchandise
    get_order_merchandises.short_description = 'Merchandise'
    get_order_merchandises.admin_order_field = 'Merchandise'

class SelectedOrderOptionChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'get_order_id',
        'get_merchandise',
        'get_merchandise_option',
        'get_merchandise_option_choice'
    )
    def get_order_id(self, obj):
        return obj.OrderOptionChoiceSelected_orderItem_key.orderItem_order_key.order_id
    get_order_id.short_description = 'Order ID'
    get_order_id.admin_order_field = 'order_id'

    def get_merchandise(self, obj):
        return obj.OrderOptionChoiceSelected_orderItem_key.orderItem_merchandise_key.merchandise
    get_merchandise.short_description = 'Merchandise'
    get_merchandise.admin_order_field = 'Merchandise'

    def get_merchandise_option(self, obj):
        return obj.OrderOptionChoiceSelected_option_key.option
    get_merchandise_option.short_description = 'Option'
    get_merchandise_option.admin_order_field = 'Option'

    def get_merchandise_option_choice(self, obj):
        return obj.OrderOptionChoiceSelected_optionChoice_key.choice
    get_merchandise_option_choice.short_description = 'Choice'
    get_merchandise_option_choice.admin_order_field = 'Choice'

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Merchandise, MerchandiseAdmin)
admin.site.register(OptionChoice, OptionChoiceAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(SelectedOrderMerchandise, SelectedOrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(SelectedOrderMerchandiseOptionChoice, SelectedOrderOptionChoiceAdmin)