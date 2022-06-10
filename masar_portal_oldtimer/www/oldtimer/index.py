import frappe

def get_context(context):
    banners = frappe.db.sql(""" SELECT name, banner_name, description, publish, image
                           FROM `tabBanners`  WHERE publish =1 ORDER BY creation DESC;""", as_dict=True)
    context.banners = banners
    return context
