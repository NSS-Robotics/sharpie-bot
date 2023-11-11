import interactions
from interactions import listen
from interactions.api.events import Startup, GuildJoin, MessageCreate
from better_profanity import profanity
import os
from dotenv import load_dotenv

from interactions import listen


load_dotenv()

bot = interactions.Client(token=os.getenv('TOKEN'), activity=interactions.Activity.create(
    name="why dogs > cats", type=interactions.ActivityType.LISTENING), intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MEMBERS | interactions.Intents.MESSAGE_CONTENT, default_scope=918591198799749240)


@listen(Startup)
async def on_startup():
    print('Ready!')
    print('------')
    profanity.load_censor_words(
        whitelist_words=['lmao', 'lmfao', 'wtf', 'omg', 'damn', 'hell', 'god', 'godamn', 'godamnit', 'goddam,', 'goddammit', 'goddamn', 'goddamned'])


@listen(GuildJoin)
async def on_guild_join(event: GuildJoin):
    print(f"Guild joined : {event.guild.name}")


@listen(MessageCreate)
async def on_message(event: MessageCreate):
    messageContent = event.message.content.lower()
    if event.message.author.id == 963255439963869244:
        return
    elif profanity.contains_profanity(messageContent):
        await event.message.reply("https://tenor.com/view/captain-america-marvel-avengers-gif-14328153")
        await event.message.author.send(f"Hi {event.message.author.mention}! Just sending this about {event.message.jump_url}. We try and keep the robotics server server pretty clean, epecially since Mr. Wong doesn't like it when we swear so if you could do your best to keep it clean that would be great! Thanks!", suppress_embeds=True)

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')
        print(f'Loaded: {filename[:-3]}')

bot.start()
