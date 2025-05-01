Feature: Add tasks to the task list

  Scenario: Add a single valid task
    Given an empty task list
    When I add a task titled "Buy milk" with priority "High" and category "Personal"
    Then the task list should contain 1 task with title "Buy milk"

  Scenario: Add multiple tasks
    Given an empty task list
    When I add a task titled "Buy milk" with priority "High" and category "Personal"
    And I add a task titled "Read book" with priority "Low" and category "School"
    Then the task list should contain 2 tasks

  Scenario: Prevent adding a task with no title
    Given an empty task list
    When I attempt to add a task with no title
    Then the task list should still be empty
