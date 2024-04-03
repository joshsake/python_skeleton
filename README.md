This is not a thorough or complete implementation of a framework, but instead an explanation of the different components that can be created.
Ideally, each of the components - core, api, ui, and db can have their own respective packages or we could start by creating a core package with shared api, ui and db functionality.

Please refer to the "Framework ideas.pdf" where I put together some examples of how I have created frameworks in the past.

The requirements.txt contains necessary Python packages.

UI is further along so after installing necessary packages and you want to run a sample test:

1. Access the terminal running your python (virtual) environment
2. Change directory to the ui folder
3. Enter "pytest" into your terminal and press Enter
4. Test for demo site "https://magento.softwaretestingboard.com/" will be ran
5. Screenshot will be saved to ui folder


References:

https://docs.pytest.org/en/8.0.x/

https://behave.readthedocs.io/en/latest/

https://plugins.jetbrains.com/plugin/9164-gherkin
