# coding=utf-8
from errbot.backends.test import FullStackTest, pushMessage, popMessage


class TestCommands(FullStackTest):
    @classmethod
    def setUpClass(cls, extra=None):
        super(TestCommands, cls).setUpClass(__file__)

    def test_borat(self):
        pushMessage('!borat')
        self.assertIn('DEVOPS_BORAT', popMessage())
