import time

from framework.webapp import WebBrowser
from maps.es_workflow_map import EsWorkflowMap
from pages.es_menu_page import EsMenuPage
from utilities.files_manipulator import FilesManipulator


class EsWorkflowPage(WebBrowser):

    def __init__(self, context):
        super().__init__(context)
        self.es_workflow_map = EsWorkflowMap()
        self.es_menu_page = EsMenuPage(self.driver)

    """
    Filter for searching something
    """

    def filter_search(self, id_workflow="", name=""):
        self.click_on(locator=self.es_workflow_map.ButtonElement("Filtro"))
        self.send_keys(locator=self.es_workflow_map.InputFieldByName(
            "Tarea", "input"), text=id_workflow)
        self.send_keys(locator=self.es_workflow_map.InputFieldByName(
            "Nombre", "input"), text=name)
        self.click_on(locator=self.es_workflow_map.ButtonElement("Búsqueda"))

    def gear_click(self, button_name):
        self.click_on(self.es_workflow_map.GearClosed())
        self.click_on(self.es_workflow_map.GearItem(button_name))

    """
    Create a workflow when is in the "Gestao de Workflow" Page
    """

    def create_workflow(self, workflow_name, sla, tmo, text_description, project):
        self.es_menu_page.click_es_menu('Administración', "Workflow")
        self.click_on(self.es_workflow_map.ButtonElement("Crear Workflow"))
        self.send_keys(self.es_workflow_map.InputFieldById(
            "Name"), workflow_name)
        self.send_keys(self.es_workflow_map.InputFieldById("SLA"), sla)
        self.send_keys(self.es_workflow_map.InputFieldById("TMO"), tmo)
        self.send_keys(self.es_workflow_map.InputFieldByName(
            "Descripción", "textarea"), text_description)
        self.select_element_by_text(
            self.es_workflow_map.SelectField("Proyecto"), project)
        self.click_on(self.es_workflow_map.ButtonElement("Guardar"))
        self.is_element_present(
            self.es_workflow_map.ValidateMessage("Detalle del workflow"))
        self.TakeScreenshot("Workflow created")

    def export_workflow(self, name_workflow_to_export=""):
        self.es_menu_page.click_es_menu('Administración', "Workflow")
        self.filter_search(name=name_workflow_to_export)
        self.gear_click("Exportación")
        time.sleep(0.2)  # To assure the download
        self.click_on(self.es_workflow_map.ModalButton("Exportación"))
        time.sleep(2)  # To assure the download
        self.TakeScreenshot("Workflow exported")

    def import_workflow_main_page(self, project, workflow_name):
        self.es_menu_page.click_es_menu('Administración', "Workflow")
        self.click_on(self.es_workflow_map.ButtonElement("Importación"))
        self.select_element_by_text(
            self.es_workflow_map.ModalSelectById("projects"), project)
        self.send_keys(self.es_workflow_map.InputFieldById(
            "nameWorkflow"), workflow_name)
        self.send_keys(self.es_workflow_map.InputFieldById("upload"),
                       FilesManipulator.SelectLastModifiedFileInPath())
        self.click_on(self.es_workflow_map.ModalButtonById("btn-importation"))
        self.is_element_present(self.es_workflow_map.ValidateMessage(
            "El nuevo flujo de trabajo creado."))
        self.TakeScreenshot("Workflow imported")
