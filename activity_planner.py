import os
from datetime import datetime
from dotenv import load_dotenv
import requests
from geopy.geocoders import Nominatim
import openai
from dateutil import parser

# Load environment variables
load_dotenv()

class ActivityPlanner:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.weather_api_key = os.getenv('WEATHER_API_KEY')
        self.geocoder = Nominatim(user_agent="activity_planner")
        self.city = "New York"  # Default city, can be changed

    def get_weather(self, date_time):
        """Get weather forecast for the specified date and time"""
        location = self.geocoder.geocode(self.city)
        
        # Get weather data from OpenWeatherMap API
        url = f"http://api.openweathermap.org/data/2.5/forecast"
        params = {
            "lat": location.latitude,
            "lon": location.longitude,
            "appid": self.weather_api_key,
            "units": "metric"
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            weather_data = response.json()
            # Find the closest weather forecast to the requested date/time
            for forecast in weather_data['list']:
                forecast_date = datetime.fromtimestamp(forecast['dt'])
                if forecast_date.date() == date_time.date():
                    return {
                        "temperature": forecast['main']['temp'],
                        "conditions": forecast['weather'][0]['description'],
                        "humidity": forecast['main']['humidity']
                    }
        return None

    def get_place_recommendation(self, activity, people_count, weather_info):
        """Get place recommendations using OpenAI"""
        prompt = f"""
        Recommend a specific place in {self.city} for {people_count} people to do {activity}.
        Weather conditions: Temperature {weather_info['temperature']}°C, {weather_info['conditions']}.
        
        Please provide:
        1. Name of the recommended place
        2. Why it's suitable for the activity
        3. Address
        4. Best features
        5. Tips for visitors
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content

    def plan_activity(self, activity, date_time_str, people_count):
        """Main function to plan an activity"""
        try:
            # Parse the date and time
            date_time = parser.parse(date_time_str)
            
            # Get weather information
            weather_info = self.get_weather(date_time)
            if not weather_info:
                return "Unable to fetch weather information"

            # Get place recommendation
            recommendation = self.get_place_recommendation(activity, people_count, weather_info)

            return {
                "weather": weather_info,
                "recommendation": recommendation
            }

        except Exception as e:
            return f"An error occurred: {str(e)}" 