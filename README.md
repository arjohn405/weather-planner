# Activity Planner

An intelligent activity planning application that provides personalized recommendations based on your activity preferences, weather conditions, and group size. The application uses OpenAI for recommendations and OpenWeatherMap for weather data.

## Features

- Activity-based recommendations
- Real-time weather information
- Group size consideration
- Modern, responsive UI
- Interactive form with validation
- Detailed recommendations with place information

## Prerequisites

Before running the application, make sure you have:

1. Python 3.8 or higher
2. Node.js 14 or higher
3. npm (Node Package Manager)
4. OpenAI API key
5. OpenWeatherMap API key

## Installation

### 1. Clone the repository


## API Keys

1. Get your OpenAI API key from: https://platform.openai.com
2. Get your OpenWeatherMap API key from: https://openweathermap.org/api

## Technologies Used

Backend:
- Flask
- OpenAI API
- OpenWeatherMap API
- Python-dotenv
- Geopy

Frontend:
- React
- Chakra UI
- Axios
- React Icons

## Error Handling

The application includes error handling for:
- API failures
- Invalid input
- Network issues
- Missing API keys

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Troubleshooting

### Common Issues:

1. **API Key Issues**
   - Ensure your API keys are correctly set in the `.env` file
   - Verify API key permissions and quotas

2. **Backend Connection Issues**
   - Verify the backend server is running on port 5000
   - Check for any CORS issues in the browser console

3. **Frontend Issues**
   - Clear npm cache: `npm cache clean --force`
   - Delete node_modules and reinstall: 
     ```bash
     rm -rf node_modules
     npm install
     ```

4. **Weather API Issues**
   - Verify your OpenWeatherMap API key is active
   - Check API call limits

For additional help, please open an issue in the repository.