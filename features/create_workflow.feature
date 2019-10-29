Feature: ES

    Scenario Outline: Create workflow
        Given I open the "<url>" url
        When I do the login in ES with <username> and <password>
        And I select the <menu> and <submenu> options in ES page
        Then I should create a workflow with "<workflow1>" "<sla>" "<tmo>" "<description>" and "<project>" variables
        Examples:
            | url                                        | username | password | menu           | submenu  | workflow1 | sla     | tmo     | description | project  |
            | http://udi-ddwy542/ES.QA.2019.1.WEB/Login/ | admin    | Adm1n@   | Administración | Workflow | Teste 68  | 0000002 | 0000007 | python bdd  | Proyecto |
