import frappe

# def sendmail(doc, recipients, msg, title, attachments=None):
#     email_args = {
#         'recipients': recipients,
#         'message': msg,
#         'subject': title,
#         'reference_doctype': doc.doctype,
#         'reference_name': doc.name,
#     }
#     if attachments:email_args['attachments']=attachments
#     # send mail
#     frappe.enqueue(method=frappe.sendmail, queue='short', timeout=300, **email_args)


def paginate(doctype, page=0, paginate_by=12):
    prev, next = 0, 0
    conditions = " "
    query = f"""SELECT ti.name, ti.item_name, ti.item_code, ti.description, ti.image, ti.disabled, tip.price_list, price_list_rate
							FROM `tab{doctype}` ti {conditions}
							inner JOIN `tabItem Price` tip
                        	ON (tip.item_code = ti.item_code AND tip.brand =ti.brand)
                        	WHERE ti.disabled= 0 AND ti.brand = 'Baja Designs' And ti.publish_on_bajadesigns = 1 AND tip.price_list = 'BajaDesigns MSRP -USD'
                        	ORDER BY ti.creation DESC """


    if(page):
        page = int(page)
        item = frappe.db.sql(query+f"""LIMIT {(page*paginate_by)-paginate_by}, {paginate_by};""", as_dict=True)
        next_set = frappe.db.sql(query+f"""LIMIT {page*paginate_by}, {paginate_by};""", as_dict=True)
        if(next_set):
            prev, next = page-1, page+1
        else:
            prev, next = page-1, 0
    else:
        count = frappe.db.sql(f"""SELECT COUNT(name) as count FROM `tab{doctype}`;""", as_dict=True)[0].count
        if(count>paginate_by):
            prev, next = 0, 2
        else:
            pass
        item = frappe.db.sql(query+f"""LIMIT {paginate_by};""", as_dict=True)
    return {
        'item': item,
        'prev': prev,
        'next': next,
    }
