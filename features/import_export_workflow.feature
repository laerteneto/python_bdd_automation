Feature: ES

    Scenario Outline: Import Export workflow
        Given I open the "<url>" url
        When I do the login in ES with <username> and <password>
        And I select the <menu> and <submenu> options in ES page
        Then I should create a workflow with "<workflow1>" "<sla>" "<tmo>" "<description>" and "<project>" variables
        When I export the "<workflow1>" workflow
        Then I should import "<workflow2>" to "<project>"
        Examples:
            | url                                        | username | password | menu           | submenu  | workflow1 | workflow2 | sla     | tmo     | description | project  |
            | http://udi-ddwy542/ES.QA.2019.1.WEB/Login/ | admin    | Adm1n@   | Administración | Workflow | Teste 98  | 98.1      | 0000002 | 0000007 | python bdd  | Proyecto |
