import interactions
from interactions import listen
from interactions.api.events import Startup
import os
from dotenv import load_dotenv

load_dotenv()

bot = interactions.Client(token=os.getenv(
    'TOKEN'), default_scope=918591198799749240)


@listen(Startup)
async def on_startup():
    print('Ready!')
    print('------')


for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')
        print(f'Loaded: {filename[:-3]}')


bot.start()
