# Shopping list with Python and Django REST Framework

## Description

This repository contains a shopping list project using the Django REST Framework. The user is able to check all the products included in the shopping list, as well as add a new product and edit or delete an existing one. It is also possible to view the details of a given product. A sqlite database was used to store the products.

## Creating a virtual environment

Open a terminal in your project directory and type the following command:

```bash
python -m venv venv
```
This will create a virtual environment named **venv**. To activate the virtual environment type the following command in your terminal:

```bash
"venv/scripts/activate.bat"
```

Next you have to install all required packages.


## Packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required packages, which are listed in the **requirements.txt** file. You can use the command below.

```bash
pip install -r requirements.txt
```



## Launch

Use the commands below to start. 

```bash
python manage.py makemigrations
python manage.py migrate
```
A description of these commands is included [here](https://docs.djangoproject.com/en/4.0/topics/migrations/).

The next step is to start the server so you can open the page in your browser. To do this use the following command.

```bash
python manage.py runserver
```


This will start the local server. Then, in a web browser, enter the address given in the terminal like:

```terminal
127.0.0.1:8000/
```

At this URL you will find the first web page of this application. It contains a description of all the endpoints available to the user. For example, to see all the products included in the shopping list, enter the following url:
 
```terminal
127.0.0.1:8000/product-list/
```
Use the json data format when adding a new product. To do this, go to:

```terminal
127.0.0.1:8000/product-create/
```

In the **Content** field, place the data in json format, for example:


```terminal
    {
        "product": "Cheese",
        "amount": 1,
        "bought": false
    }
```

Then press **POST** and check the list of all products again. 

Editing an existing product is done in the same way. In this case, copy the product data and then use the endpoint:

```terminal
http://127.0.0.1:8000/product-update/id/
```

And in the field **Content** paste the product information with the changed fields. Be sure not to include the **id** field, as it cannot be changed.

## Closing words

Further development of the application may involve making the front end of the site using for example the React.js library combined with DRF.
