import telegram
import requests

# Set up your bot with the Telegram Bot API
bot = telegram.Bot('YOUR_BOT_TOKEN')

# Define a function to handle incoming messages
def handle_message(update, context):
    # Get the location from the user's message
    location = update.message.text

    # Use the OpenWeatherMap API to get weather data for the location
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid=YOUR_API_KEY'
    response = requests.get(url).json()

    # Parse the weather data and format it into a message
    temperature = round(response['main']['temp'] - 273.15, 1)  # Convert temperature from Kelvin to Celsius
    weather_description = response['weather'][0]['description']
    message = f'The temperature in {location} is {temperature} degrees Celsius and the weather is {weather_description}.'

    # Send the message back to the user through the Telegram Bot API
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=message)

# Set up a handler for incoming messages
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

# Start the bot
updater.start_polling()
updater.idle()
