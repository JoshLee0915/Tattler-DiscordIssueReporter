from discord.ext import commands
from TattlerDIR import TattlerConfigManager


class TattlerBot:

    def __init__(self, bot, tracker_manager):
        self.bot = bot
        self.configManager = TattlerConfigManager.ConfigManager()
        self.configManager.load()
        self.trackerManager = tracker_manager

    @commands.command(pass_context=True)
    async def bug(self, context, *, message):
        if not self.channel_valid(context.message.channel, 'report_channel'):
            await self.bot.say('To report bugs please use {}'.format(self.configManager.Discord['reportchannel']))
            return

        message_parts = TattlerBot.parse_message(message)
        if len(message_parts) < 2:
            await self.bot.say(
                'Invalid message format.\nPlease follow format: <command> <issue summery>\n<issue details>')
            return

        user = str(context.message.author)
        issue = self.trackerManager.create_bug(discord=context.message.server.name,
                                               username=user,
                                               title=message_parts['summery'],
                                               body=message_parts['details'])

        await self.bot.say('Bug: {title} was created with id {id}', title=message_parts['summery'], id=issue['id'])

    @commands.command(pass_context=True)
    async def request(self, context, *, message):
        if not self.channel_valid(context.message.channel, 'report_channel'):
            await self.bot.say('To request a feature please use {}'.format(self.configManager.Discord['reportchannel']))
            return

        message_parts = TattlerBot.parse_message(message)
        if len(message_parts) < 2:
            await self.bot.say(
                'Invalid message format. Please follow format <command> <issue summery>\n<issue details>')
            return

        user = str(context.message.author)
        issue = self.trackerManager.create_request(discord=context.message.server.name,
                                                   username=user,
                                                   title=message_parts['summery'],
                                                   body=message_parts['details'])

        await self.bot.say('Request: {title} was created with id {id}', title=message_parts['summery'], id=issue['id'])

    def channel_valid(self, channel, config_tag):
        return self.configManager.Discord[config_tag] == 'ANY' or self.configManager.Discord[config_tag] == channel.name

    @staticmethod
    def parse_message(message):
        summary_eol = message.find('\n')
        if summary_eol == -1 or summary_eol >= len(message) - 1:
            return {}

        summary = message[:summary_eol].strip()
        details = message[summary_eol:].strip()

        return {'summery': summary, 'details': details}
