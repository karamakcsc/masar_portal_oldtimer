import frappe

def get_context(context):
    context.detail = frappe.get_doc('Item', 'AKRA-P-HSY10SO6')
    return context
