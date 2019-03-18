import TattlerDIR
from TattlerDIR import TattlerConfigManager
from TattlerDIR.TattlerTrackerManager import TattlerTrackerManager
from TattlerDIR.Trackers.YouTrackTracker import YouTrackTracker

from discord.ext import commands


bot = commands.Bot(command_prefix='!')
config_manager = TattlerConfigManager.ConfigManager()


@bot.event
async def on_ready():
    if config_manager.Discord_Optional['announcement_channel'] != '':
        for server in bot.connection.servers:
            for channel in server.channels:
                if channel.name == config_manager.Discord_Optional['announcementchannel']:
                    await bot.send_message(channel, 'Tattler online!')
                    break

    print("Tattler is active")


if __name__ == '__main__':
    config_manager.load()
    TattlerDIR.trackerManager = TattlerTrackerManager(config_manager)

    TattlerDIR.trackerManager.register_issue_tracker('YouTrack', YouTrackTracker)

    for project in config_manager.General['projects']:
        TattlerDIR.trackerManager.register_project(project)

    bot.load_extension("TattlerDIR")

    bot.run(config_manager.Discord['token'])
