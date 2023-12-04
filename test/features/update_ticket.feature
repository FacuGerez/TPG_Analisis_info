Feature: As a support employee, I want to be able to update tickets to keep information up to date

  Scenario: Support employee decides to update some field of a ticket and successfully modifies it
    Given a support employee wants to update some allowed field(s) of a ticket (severity, priority, status, name, description)
     When they choose to change them and you try to apply this
     Then the ticket is update successfully

  Scenario: Support employee tries to update some field of a ticket without providing a description
    Given a support employee wants to update some allowed field(s) of a ticket and does not provide a description
    When they choose to change them and you try to apply this
    Then the employee is informed that it is necessary not to leave the description empty

  Scenario: Support employee tries to update some field of a ticket without selecting a severity
    Given a support employee wants to update some allowed field(s) of a ticket and does not select a severity
    When they choose to change them and you try to apply this
    Then the employee is informed that a severity needs to be selected

  Scenario: Support employee tries to update some field of a ticket without selecting a priority
    Given a support employee wants to update some allowed field(s) of a ticket and does not select a priority
    When they choose to change them and you try to apply this
    Then the employee is informed that a priority needs to be selected