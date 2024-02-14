# Azure Function Webpage

This project is a webpage created using Azure Functions.

## Description

The Azure Function in this project serves to handle HTTP requests and returns an HTML page in response to GET requests. The webpage contains a stylized user interface with various elements such as a menu, icons, and content sections.

## Installation

To run this project, you will need to:

1. Install [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#v2).
2. Clone this repository.
3. Run `func init` to initialize the az function
4. Run the function locally using the command `func start`.
5. Deploy your function using GitHub Actions or running `func azure functionapp publish your_function_app_name`

## Usage

Send a GET request to your function's URL to receive the HTML page.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```