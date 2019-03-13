from discord.ext import commands
from TattlerDIR import TattlerConfigManager

class TattlerBot:

    def __init__(self, bot):
        self.bot = bot
        self.configManager = TattlerConfigManager.ConfigManager()
        self.configManager.load()

    @commands.command(pass_context=True)
    async def bug(self, context, *, message):
        if not self.channel_valid(context.message.channel, 'reportchannel'):
            await self.bot.say("To report bugs please use {}".format(self.configManager.Discord['reportchannel']))
            return
        # TODO: Add a call that adds a bug to youtrack
        await self.bot.say("Reporting Bug!")
        pass

    @commands.command(pass_context=True)
    async def request(self, context, *, message):
        if not self.channel_valid(context.message.channel, 'reportchannel'):
            await self.bot.say("To request a feature please use {}".format(self.configManager.Discord['reportchannel']))
            return
        # TODO: Add a call that adds a request to youtack
        await self.bot.say("Adding Request!")
        pass

    def channel_valid(self, channel, config_tag):
        return self.configManager.Discord[config_tag] == 'ANY' or self.configManager.Discord[config_tag] == channel.name

