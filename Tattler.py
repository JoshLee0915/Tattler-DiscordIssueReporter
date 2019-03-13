from TattlerDIR import TattlerConfigManager
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
config_manager = TattlerConfigManager.ConfigManager()


@bot.event
async def on_ready():
    if config_manager.Discord_Optional['announcementchannel'] != '':
        for server in bot.connection.servers:
            for channel in server.channels:
                if channel.name == config_manager.Discord_Optional['announcementchannel']:
                    await bot.send_message(channel, 'Tattler online!')
                    break

    print("Tattler is active")


if __name__ == '__main__':
    config_manager.load()
    bot.load_extension("TattlerDIR")

    bot.run(config_manager.Discord['token'])
