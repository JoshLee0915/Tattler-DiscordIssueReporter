import TattlerDIR.TattlerBot

trackerManager = None


def setup(bot):
    if not trackerManager:
        print('A tracker manager must be set. Terminating...')
        raise Exception
    bot.add_cog(TattlerBot.TattlerBot(bot, trackerManager))
