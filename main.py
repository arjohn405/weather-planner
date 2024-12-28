from activity_planner import ActivityPlanner
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print("API is working:", response)
except Exception as e:
    print("Error:", e)

def main():
    planner = ActivityPlanner()
    
    print("Welcome to the Activity Planner!")
    print("--------------------------------")
    
    # Get user input
    activity = input("What activity would you like to do? (e.g., hiking, dining, shopping): ")
    date_time = input("When would you like to do this? (YYYY-MM-DD HH:MM): ")
    people_count = input("How many people will be participating?: ")
    
    # Get recommendations
    result = planner.plan_activity(activity, date_time, int(people_count))
    
    # Display results
    print("\nHere's your personalized recommendation:")
    print("----------------------------------------")
    print(f"\nWeather Forecast:")
    print(f"Temperature: {result['weather']['temperature']}°C")
    print(f"Conditions: {result['weather']['conditions']}")
    print(f"Humidity: {result['weather']['humidity']}%")
    
    print("\nRecommendation:")
    print(result['recommendation'])

if __name__ == "__main__":
    main() 