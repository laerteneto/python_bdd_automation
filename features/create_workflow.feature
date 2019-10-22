Feature: ES

    Scenario Outline: Create workflow
        Given I open the "<url>" url
        When I do the login in ES with <username> and <password>
        And I select the <menu> and <submenu> options in ES page
        Then I should create a workflow with <name> <version> <subversion> <description> and <projeto> variables
        Examples:
            | url                                |
            | https://the-internet.herokuapp.com |
