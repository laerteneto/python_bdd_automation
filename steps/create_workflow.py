from behave import given, then, when

from pages.es_login_page import EsLoginPage
from pages.es_menu_page import EsMenuPage
from pages.es_workflow_page import EsWorkflowPage


@when(u'I do the login in ES with {username} and {password}')
def step_impl(context, username, password):
    es_login = EsLoginPage(context)
    es_login.login(username, password)


@when(u'I select the {menu} and {submenu} options in ES page')
def step_impl(context, menu, submenu):
    es_menu = EsMenuPage(context)
    es_menu.click_es_menu(menu, submenu)


@then(u'I should create a workflow with "{workflow1}" "{sla}" "{tmo}" "{description}" and "{project}" variables')
def step_impl(context, workflow1, sla, tmo, description, project):
    es_workflow = EsWorkflowPage(context)
    es_workflow.create_workflow(workflow1, sla, tmo, description, project)
