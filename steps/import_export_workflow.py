import time

from behave import given, then, when

from pages.es_login_page import EsLoginPage
from pages.es_workflow_page import EsWorkflowPage


@when(u'I export the "{workflow1}" workflow')
def step_impl(context, workflow1):
    es_workflow = EsWorkflowPage(context)
    es_workflow.export_workflow(workflow1)


@then(u'I should import "{workflow2}" to "{project}"')
def step_impl(context, workflow2, project):
    es_workflow = EsWorkflowPage(context)
    es_workflow.import_workflow_main_page(project, workflow2)
