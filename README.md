# SF-FoodTruck-Django

## Overview
This project is a sample food truck locator for the city of San Francisco. It allows a user to insert coordinates (latitude and longitude) within a limited range of San Francisco and returns a list of the five nearest active food trucks. The active food trucks are loaded from a publicly available spreadsheet, which contains information about each food truck (name, type of food, coordinates, etc.). Only a small subset of the publicly available information on each truck is actually used.

## Implementation
The food truck locator was developed with the following tools/frameworks:
- Django
- PostgresQL
- JavaScript
- HTML
- Bootstrap
The application was developed to include a GUI-based web interface and an open api (no API keys needed) that returns food truck data in JSON format

## Usage
### Requirements
Python 3.7.4
### Installation
- Clone this repository
- Navigat to the *food_truck_locator* directory
- Create a virtual environment
- At the command line, run the command *pip install requirements.txt* to install the needed software components. The list of components includes several items not needed specifically for this app because I did not develop it in a virtual environment.
### Running the app
To run the app locally, navigate to the top level directory of the project and type the command: *python manage.py runserver*. The path to the development server will show up at the prompt. Open a web browser and type in the path in the search bar. This should take you to the app home page, which lists all active food trucks alongside a couple of searchboxes.
### Finding a food truck
Type in coordinate values for longitude and latitude, then click 'Find nearest food truck'.  A page will be generated showing the 5 nearest food trucks to the location specified by the entered coordinates.
### Using the API
A JSON response listing the five nearest food trucks to any location can be found by entering the following path in a browser's search bar when the app is run locally: *http://127.0.0.1:8000/api/latitude/longitude/number_of_results_to_return*. For example, the command *http://127.0.0.1:8000/api/37.780/-122.41/6* returns a JSON response with data for the 6 nearest restaurants to the location with latitude 37.780 and longitude -122.41.
### Try out the app without installing it
This app has been deployed using Heroku and can be accessed at: 
- *https://sf-ft-nudoyen.herokuapp.com/* (GUI interface)
- *https://sf-ft-nudoyen.herokuapp.com/api/latitude/longitude/number_of_results_to_return* (API) eg., *https://sf-ft-nudoyen.herokuapp.com/api/37.780/-122.41/6*
