Feature: Verifying that behave is installed

    Scenario: Run a sample test
        Given we have behave installed
        When we implement a test
        Then behave will run the test for us

