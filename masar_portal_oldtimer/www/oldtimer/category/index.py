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
	# cat_th = frappe.db.sql(f""" Select  titc.name, titc.first_category, titc.second_category, titc.third_category,
	# 						tisc.name, tisc.first_category, tisc.second_category
	# 						From `tabItem Third Category` titc, `tabItem Second Category` tisc
	# 						WHERE
	# 						titc.first_category = 'Cars'
	# 						AND titc.second_category = tisc.'{context.cat_nd.name}'
	# 						""" , as_dict=True)
	context.cat_th = cat_th




	# select
	# 	"Journal Entry" as reference_type, t1.name as reference_name,
	# 	t1.posting_date, t1.remark as remarks, t2.name as reference_row,
	# 	{dr_or_cr} as amount, t2.is_advance,
	# 	t2.account_currency as currency
	# from
	# 	`tabJournal Entry` t1, `tabJournal Entry Account` t2
	# where
	# 	t1.name = t2.parent and t1.docstatus = 1 and t2.docstatus = 1
	# 	and t2.party_type = %(party_type)s and t2.party = %(party)s
	# 	and t2.account = %(account)s and {dr_or_cr} > 0 {condition}
	# 	and (t2.reference_type is null or t2.reference_type = '' or
	# 		(t2.reference_type in ('Sales Order', 'Purchase Order')
	# 			and t2.reference_name is not null and t2.reference_name != ''))
	# 	and (CASE
	# 		WHEN t1.voucher_type in ('Debit Note', 'Credit Note')
	# 		THEN 1=1
	# 		ELSE {bank_account_condition}
	# 	END)
	# order by t1.posting_date
	# """.format(


	#paginate Rule
	page = frappe.form_dict.page
	pagination = paginate('Item', page)
	context.item = pagination.get('item')
	context.prev = pagination.get('prev')
	context.next = pagination.get('next')

	return context
