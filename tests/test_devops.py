# coding=utf-8
from errbot.backends.test import FullStackTest, pushMessage, popMessage


class TestCommands(FullStackTest):

    def test_borat(self):
        pushMessage('!borat')
        self.assertIn('DEVOPS_BORAT', popMessage())
