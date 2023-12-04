Feature: As a support employee, I want to be able to delete tickets to discontinue unnecessary tickets
    Scenario: the support employee decides to delete a ticket and does so successfully
      Given a support employee wants to delete a ticket
       When you decide to delete the ticket
       Then the ticket is deleted successfully.
