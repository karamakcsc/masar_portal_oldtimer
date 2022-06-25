import frappe

from masar_portal_oldtimer.utils import paginate
def get_context(context):
	#Banners Loop
	# item = frappe.db.sql(""" SELECT ti.name, ti.item_name, ti.item_code, ti.description, ti.image, ti.disabled, tip.price_list, price_list_rate
	# 						FROM `tabItem` ti
	# 						inner JOIN `tabItem Price` tip
	# 						ON (tip.item_code = ti.item_code AND tip.brand =ti.brand)
	# 						WHERE ti.disabled= 0 AND ti.brand = 'Baja Designs' AND tip.price_list = 'BajaDesigns MSRP -USD'
	# 						ORDER BY ti.creation DESC LIMIT 12;""", as_dict=True)
	# context.item = item

	#Second Category Loop
	cat_nd = frappe.db.sql(""" SELECT name, creation, first_category, second_category
						   FROM `tabItem Second Category`  WHERE first_category ='Cars' ORDER BY creation DESC ;""", as_dict=True)
	context.cat_nd = cat_nd

	#Thired Category Loop
	cat_th = frappe.db.sql(f""" SELECT name, creation, first_category, second_category, third_category
						   FROM `tabItem Third Category`  WHERE first_category = 'Cars'  """ , as_dict=True)
	context.cat_th = cat_th


	#paginate Rule
	page = frappe.form_dict.page
	pagination = paginate('Item', page)
	context.item = pagination.get('item')
	context.prev = pagination.get('prev')
	context.next = pagination.get('next')

	return context
