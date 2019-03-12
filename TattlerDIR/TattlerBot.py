from discord.ext import commands


class TattlerBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='!')

    async def on_ready(self):
        pass

    @commands.command()
    async def help(self, context):
        pass

    @commands.command()
    async def bug(self, context, *, args):
        pass

    @commands.command()
    async def request(self, context, *, args):
        pass
