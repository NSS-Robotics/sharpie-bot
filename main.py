import interactions
from interactions import Client, Intents
import os
from dotenv import load_dotenv

load_dotenv()

bot = Client(token=os.getenv('TOKEN'), presence=interactions.ClientPresence(activities=[interactions.PresenceActivity(name="Safety Third", type=interactions.PresenceActivityType.LISTENING)]), intents=Intents.GUILD_MESSAGE_CONTENT)

@bot.event
async def on_ready():
    print('Ready!')
    print('------')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        print(f'Loaded: {filename[:-3]}')
        bot.load(f'commands.{filename[:-3]}')

bot.start()
