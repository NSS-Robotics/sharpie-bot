import interactions


class Annoy(interactions.Extension):
    def __init__(self, bot: interactions.Client):
        self.bot: interactions.Client = bot

    @interactions.slash_command(
        name="annoy",
        description="Annoy someone",
    )
    @interactions.slash_option(
        name="user",
        description="The user to annoy",
        opt_type=interactions.OptionType.USER,
        required=True
    )
    @interactions.slash_option(
        name="amount",
        description="The amount of times to annoy the user",
        opt_type=interactions.OptionType.INTEGER,
        required=True
    )
    async def annoy(
        self,
        ctx: interactions.SlashContext,
        user,
        amount: int,
    ) -> None:
        if amount > 10:
            await ctx.send("That's just too far")
            return
        else:
            for i in range(amount):
                await ctx.send(user.mention)


def setup(bot):
    Annoy(bot)
