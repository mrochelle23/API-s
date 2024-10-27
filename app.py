from flask import Flask, request, render_template
import requests
from pprint import PrettyPrinter

#Flask App
app = Flask(__name__)

#Home Page
@app.route('/', methods=['GET'])
def homePage():
    return render_template('swapi_form.html')

#Accessing the Star Wars API
SWAPI_URL = "https://swapi.py4e.com/api/people/"
pp = PrettyPrinter(indent=4)

@app.route('/swapi', methods=['GET', 'POST'])
def swapi():
    if request.method == 'POST':
        character_id = request.form.get('character_id')
        print(f'Received character_id: {character_id}')
        
        #API Request
        response = requests.get(f'{SWAPI_URL}/{character_id}/')
        print(f'API response: {response.status_code}')

        #Recording the API Response Into JSON File
        if response.status_code == 200:
            record = response.json()
            context = {
                'record': record,
            }
        else:
            #Error Handling
            context = {
                'error': 'Character cannot be located'
            }
            return render_template('swapi_results.html', **context)
        
        #Recording the API Response Into JSON File
        record = response.json()
        context = {
        'record': record,
        }
        #pp.pprint(record)
        return render_template('swapi_results.html', **context)
    else:
        #Error Handling
        context = {
            'error': 'Character cannot be located'
            }
        return render_template('swapi_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
