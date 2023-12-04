Feature: As a support employee, I want to be able to update tickets to report issues that arise

  Scenario: Support employee decides to update some field of a ticket and successfully modifies it
    Given a support employee wants to update some allowed field(s) of a ticket (severity, priority, status, name, description)
     When they choose to change them and you try to apply this
     Then the ticket is update successfully