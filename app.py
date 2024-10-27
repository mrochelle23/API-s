from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Main route to render the form
@app.route('/', methods=['GET', 'POST'])
def index():
    character_data = None
    error_message = None
    
    if request.method == 'POST':
        char_id = request.form.get('character_id')
        if char_id:
            swapi_url = f'https://swapi.py4e.com/api/people/{char_id}'
            response = requests.get(swapi_url)
            
            # Check if request is successful
            if response.status_code == 200:
                data = response.json()
                character_data = {
                    'name': data.get('name'),
                    'height': data.get('height'),
                    'mass': data.get('mass'),
                    'hair_color': data.get('hair_color'),
                    'eye_color': data.get('eye_color')
                }
                
                # Fetch homeworld
                homeworld_url = data.get('homeworld')
                if homeworld_url:
                    homeworld_response = requests.get(homeworld_url)
                    if homeworld_response.status_code == 200:
                        homeworld_data = homeworld_response.json()
                        character_data['homeworld'] = homeworld_data.get('name')
                
                # Fetch films
                film_titles = []
                for film_url in data.get('films', []):
                    film_response = requests.get(film_url)
                    if film_response.status_code == 200:
                        film_data = film_response.json()
                        film_titles.append(film_data.get('title'))
                character_data['films'] = film_titles

            else:
                error_message = "Character not found or an error occurred."

    return render_template('index.html', character_data=character_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
