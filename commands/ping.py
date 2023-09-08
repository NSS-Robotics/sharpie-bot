import interactions

GUILD_IDS = [918591198799749240]


class Ping(interactions.Extension):
    def __init__(self, bot: interactions.Client) -> None:
        self.bot = bot

    @interactions.slash_command(name="ping", description="Shows bot latency")
    async def ping(self, ctx) -> None:
        await ctx.send("Hello! I'm Herbert!", ephemeral=True)


def setup(bot: interactions.Client) -> None:
    Ping(bot)
