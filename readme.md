# SWAPI Flask App

This Flask application allows users to interact with the Star Wars API (SWAPI) to retrieve information about characters from the Star Wars universe. Users can input a character ID and receive details such as name, height, mass, hair color, and eye color.

## Features

- **Character Lookup**: Input a Star Wars character ID to fetch details from SWAPI.
- **User-Friendly Interface**: Simple HTML forms for easy interaction.

## Technologies Used

- **Python**: Backend logic implemented using Flask.
- **HTML**: Templates for rendering user interface.

## Project Structure

```
/swapi_flask_app
├── app.py                 # Main application file
├── firstRequests.py       # Test script to make requests to the app
├── templates              # Directory for HTML templates
│   ├── base.html          # Base template for consistent layout
│   ├── swapi_form.html    # Form for user input (character ID)
│   └── swapi_results.html  # Template for displaying results
└── swapi.json             # Sample data (if needed for testing)
```

## Templates

### `base.html`

This is the base template that provides a consistent layout for all pages in the application. It includes placeholders for title and content that can be overridden in other templates.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
    {% block content %}{% endblock %}
    </body>
</html>
```

### `swapi_form.html`

This template allows users to input a Star Wars character ID. It extends the base template and provides a form that submits to the `/swapi` endpoint.

```html
{% extends 'base.html' %}

{% block title %}
Star Wars API
{% endblock %}

{% block content %}
<h1>Star Wars API</h1>
<form action="/swapi" method="POST">
    <fieldset>
        <legend>Star Wars Info:</legend>
        <p>
            <label>
                Type in a Star Wars character ID:
                <input type="text" id="character_id" name="character_id"><br><br>
            </label>
        </p>
        <input type="submit" value="Search for API">
    </fieldset>
</form>
{% endblock %}
```

### `swapi_results.html`

This template displays the results fetched from SWAPI based on the user’s input. If the character is not found, an appropriate message is displayed.

```html
{% extends 'base.html' %}

{% block title %}
Star Wars Results
{% endblock %}

{% block content %}
<h1>SWAPI Results</h1>
   
{% if record.detail == 'Not found' %}
    <p>Data Not Found</p>
{% else %}
    <section>
        <p>
            Name: {{record.name}}
        </p>
        <p>
            Height: {{record.height}}
        </p>
        <p>
            Mass: {{record.mass}}
        </p>
        <p>
            Hair Color: {{record.hair_color}}
        </p>
        <p>
            Eye Color: {{record.eye_color}}
        </p>
    </section>
{% endif %}
{% endblock %}
```

## How to Run the Application

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install the required dependencies, if any, using pip:
   ```bash
   pip install flask requests
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Testing the Application

You can use the `firstRequests.py` script to test the application locally by making a GET request to the home page.

```python
import requests

result = requests.get("http://127.0.0.1:5000/")
print("Base result print:", result)
result_json = result.json()
print(result_json)
```
