Feature: As a support employee, I want to be able to create tickets to report issues that arise

  Scenario: Support employee receives a complaint from a customer and successfully creates a ticket
    Given a support employee wants to log a ticket and fills out all required fields
     When they want to record the complaint in a ticket
     Then the ticket is created successfully

