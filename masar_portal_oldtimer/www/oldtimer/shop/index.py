# import frappe
#
# def get_context(context):
#     # print(f"\n\n\n\n{frappe.form_dict}\n\n\n\n")
#     # try:
#         docname = frappe.form_dict.docname
#         context.property = frappe.get_doc("Item", frappe.form_dict.docname)
#         context.agent = frappe.get_doc("Agent", context.property.agent)
#         related_items = frappe.db.sql(f"""
#             SELECT creation, name, item_name, item_code, description, image,
#             image FROM `tabItem` WHERE item_name='{context.item.item_name}'
#               ORDER BY creation DESC LIMIT 3;
#             """, as_dict=True)
#         context.item = item
#
#     # except Exception as e:
#     #     frappe.local.flags.redirect_location = '/404'
#     #     raise frappe.Redirect
#
#         return context
#
# # SELECT ti.name, ti.item_name, ti.item_code, ti.description, ti.image, ti.disabled, tip.price_list, price_list_rate
# #                         FROM `tab{doctype}` ti {conditions}
# #                         inner JOIN `tabItem Price` tip
# #                         ON (tip.item_code = ti.item_code AND tip.brand =ti.brand)
# #                         WHERE ti.disabled= 0 AND ti.brand = 'Baja Designs' AND tip.price_list = 'BajaDesigns MSRP -USD'
# #                         ORDER BY ti.creation DESC """
