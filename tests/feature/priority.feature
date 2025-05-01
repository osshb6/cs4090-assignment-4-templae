Feature: Filter and update task priority

  Scenario: Filter tasks by priority
    Given tasks with priorities High, Low, Low
    When I filter tasks by priority "Low"
    Then I should get 2 tasks

  Scenario: Set task priority
    Given a task with priority "Low"
    When I change the task priority to "High"
    Then the task should have priority "High"