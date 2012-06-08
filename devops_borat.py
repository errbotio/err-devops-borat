from random import choice
from feedparser import parse
from errbot.botplugin import BotPlugin
from errbot.jabberbot import botcmd

class DevOpsBorat(BotPlugin):
    @botcmd
    def borat(self, mess, args):
        myfeed = parse('http://api.twitter.com/1/statuses/user_timeline.rss?screen_name=DEVOPS_BORAT')
        items = myfeed['entries']
        return choice(items).description

    @botcmd
    def jesus(self, mess, args):
        myfeed = parse('http://api.twitter.com/1/statuses/user_timeline.rss?screen_name=devops_jesus')
        items = myfeed['entries']
        return choice(items).description

    @botcmd
    def yoda(self, mess, args):
        myfeed = parse('http://api.twitter.com/1/statuses/user_timeline.rss?screen_name=UXYoda')
        items = myfeed['entries']
        return choice(items).description
