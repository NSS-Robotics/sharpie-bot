import interactions
from interactions import ButtonStyle


class Media(interactions.Extension):
    def __init__(self, bot: interactions.Client) -> None:
        self.bot = bot

    @interactions.slash_command(name="media", description="Links for the places with all the robotics media")
    async def image(self, ctx) -> None:
        flickrBtn = interactions.Button(
            style=(ButtonStyle.URL),
            label="Flickr",
            emoji=interactions.PartialEmoji.from_str(
                "<:flickr:1149691826354278410>"),
            url="https://flickr.com/knightowls"
        )
        websiteBtn = interactions.Button(
            style=(ButtonStyle.URL),
            label="Website",
            emoji=interactions.PartialEmoji.from_str("🌐"),
            url="https://knightowls.ca/gallery"
        )
        embed = interactions.Embed(
            title="📸 Robotics Media",
            description="All of the pictures and videos we've taken have been uploaded to our Flickr and our website",
        )
        await ctx.send(embeds=embed, components=[flickrBtn, websiteBtn], ephemeral=True)


def setup(bot: interactions.Client) -> None:
    Media(bot)
