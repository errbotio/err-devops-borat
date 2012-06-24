from random import choice
from feedparser import parse
from errbot.botplugin import BotPlugin
from errbot.jabberbot import botcmd

class DevOpsBorat(BotPlugin):
    """
    Quotes from various dev humour related twitter accounts
    """
    @botcmd
    def borat(self, mess, args):
        """
        Random quotes from the DEVOPS_BORAT twitter account
        """
        myfeed = parse('http://api.twitter.com/1/statuses/user_timeline.rss?screen_name=DEVOPS_BORAT')
        items = myfeed['entries']
        return choice(items).description

    @botcmd
    def jesus(self, mess, args):
        """
        Random quotes from the devops_jesus twitter account
        """
        myfeed = parse('http://api.twitter.com/1/statuses/user_timeline.rss?screen_name=devops_jesus')
        items = myfeed['entries']
        return choice(items).description

    @botcmd
    def yoda(self, mess, args):
        """
        Random quotes from the UXYoda twitter account
        """
        myfeed = parse('http://api.twitter.com/1/statuses/user_timeline.rss?screen_name=UXYoda')
        items = myfeed['entries']
        return choice(items).description
