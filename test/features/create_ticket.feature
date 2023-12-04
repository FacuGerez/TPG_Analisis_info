Feature: As a support employee, I want to be able to create tickets to report issues that arise

  Scenario: Support employee receives a complaint from a customer and successfully creates a ticket
    Given a support employee wants to log a ticket and fills out all required fields
     When they want to record the complaint in a ticket
     Then the ticket is created successfully

  Scenario: Support employee tries to create a ticket without providing a description
    Given a support employee wants to register a ticket and does not provide a description
     When they want to record the complaint in a ticket
     Then the employee is informed that a description needs to be added and is asked to complete it

  Scenario: Support employee tries to create a ticket without selecting a severity
    Given a support employee wants to register a ticket and does not select a severity
     When they want to record the complaint in a ticket
     Then the employee is informed that a severity needs to be selected and is asked to select it

  Scenario: Support employee tries to create a ticket without selecting a priority
    Given a support employee wants to register a ticket and does not select a priority
     When they want to record the complaint in a ticket
     Then the employee is informed that a priority needs to be selected and is asked to select it