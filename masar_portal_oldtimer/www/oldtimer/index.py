import frappe

def get_context(context):
	#Banners Loop
	banners = frappe.db.sql(""" SELECT name, banner_name, description, publish, image
						   FROM `tabBanners`  WHERE publish =1 ORDER BY creation DESC;""", as_dict=True)
	context.banners = banners

	#Blogs Loop
	blog = frappe.db.sql(""" SELECT name, creation, title, blog_intro, published, published_on, meta_image, content
						   FROM `tabBlog Post`  WHERE published =1 ORDER BY creation DESC LIMIT 3;""", as_dict=True)
	context.blog = blog




	return context
