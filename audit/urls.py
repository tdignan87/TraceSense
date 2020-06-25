from django.urls import path
from audit.views import new_audit, audit_list,update_audit,delete_audit,open_actions

urlpatterns = [
  path("questions/",new_audit,name="new_audit"),
  path("view_audits/",audit_list,name="list_audits"),
  path("edit_audits/<str:pk>",update_audit,name="update_audits"),
  path("delete_audits/<str:pk>",delete_audit,name="delete_audit"),
  path("open_actions/",open_actions,name="open_actions"),
]