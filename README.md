# Python technical challenge - Jungsoft

## Challenge description

You are the owner of a retail shop. You buy products from an e-commerce platform to resell them.
This app will be build to collect and transform information from the e-commerce platform.

The e-commerce platform is located in this project, at /pages/content.html.
You can open it on your browser to see how it looks like.

## Requirements

The app should be available through a rest API.
A basic endpoint is already set up at app/main.py. You should create more to achieve the requirements below.

List of requirements:
  - Using the API:
    - Allow the user to get a list of all products from the e-commerce platform, and present them in a structured way.
    - Each product listed, should be structured so that only the information below is shown:
        - name (type: string).
        - price (type: float).
        - best_seller (type: boolean).
          - This is true when the label "Mais vendida" is present on the product.
        - rating (type: float).
    - There should be a way to list only the best-selling products.
    - There should be a way to list only the products with a rating higher than a given value.
    - Allow the user to extract information of a single product, given its name.

## Optional

Propose a simple interface to your script that could be used to collect information from similar e-commerce platforms.

Suggestion:
There could be a generic class which is inherited by each class that collects and parses information from a web site.

## Recommendations

As suggested at controller/main.py, using bs4 to parse the HTML is a good option.

## At last

* Write down any assumptions you need to make.
* Feel free to change the code that came with this repository,
and make sure you have well documented, structured and presentable work.

## Setting up your development environment

### Installing the libraries
At the same directory as this file, run:
  - `pip install pipenv`
  - `pipenv install`

### Running the API for development
Initialize your app using `pipenv`:

- `pipenv shell`

Then run the following commands:

- `uvicorn app.main:app --reload`

And your app will be running on http://localhost:8000/

Tip:

Access http://localhost:8000/docs to use the built-in interface.
