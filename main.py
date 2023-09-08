import interactions
from interactions import listen
from interactions.api.events import Startup, GuildJoin
import os
from dotenv import load_dotenv

from interactions import listen


load_dotenv()

bot = interactions.Client(token=os.getenv('TOKEN'), activity=interactions.Activity.create(
    name="Safety Third", type=interactions.ActivityType.LISTENING), intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MEMBERS, default_scope=918591198799749240)


@listen(Startup)
async def on_startup():
    print('Ready!')
    print('------')


@listen(GuildJoin)
async def on_guild_join(event: GuildJoin):
    print(f"Guild joined : {event.guild.name}")


for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')
        print(f'Loaded: {filename[:-3]}')


bot.start()
