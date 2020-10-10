Feature: To Test the function of Twitter

  Scenario: User logs into twitter with username and password
    Given User navigates to twitter login page
    When User enters username, password and clicks sign-in button
    Then User is taken to dashboard

  Scenario: User searches for celebrity and logs his followings into csv file
    Given User navigates to twitter login page
    When User enters username, password and clicks sign-in button
    And User searches for his/her favourite celebrity
    And User is taken to Celebrity page and clicks on following
    Then User Copies all people in the following list to csv file

