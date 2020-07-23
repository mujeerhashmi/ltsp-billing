# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cimec_infotech"
app_title = "Cimec Infotech"
app_publisher = "4C Solutions"
app_description = "Cimec Infotech Customisations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@4csolutions.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cimec_infotech/css/cimec_infotech.css"
# app_include_js = "/assets/cimec_infotech/js/cimec_infotech.js"

# include js, css files in header of web template
# web_include_css = "/assets/cimec_infotech/css/cimec_infotech.css"
# web_include_js = "/assets/cimec_infotech/js/cimec_infotech.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "cimec_infotech.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cimec_infotech.install.before_install"
# after_install = "cimec_infotech.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cimec_infotech.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cimec_infotech.tasks.all"
# 	],
# 	"daily": [
# 		"cimec_infotech.tasks.daily"
# 	],
# 	"hourly": [
# 		"cimec_infotech.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cimec_infotech.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cimec_infotech.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "cimec_infotech.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cimec_infotech.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "cimec_infotech.task.get_dashboard_data"
# }

