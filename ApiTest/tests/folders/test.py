import pytest

from tools.helper import Helper
from lib.folders_lib import add_folders
from cfg.folders.config import folders_config as cfg

from core import CoreTests
# [{"name":"test","parent":-1,
# "only_web":false,"archive":false,
# "type":"user","id":null,"system":false,
# "open":true,"security":false,"messages_total":0,
# "messages_unread":0,"child":false,"children":false,"collapse":false}]
class TestFolders(CoreTests):
    @classmethod
    def setup_class(cls):
        cls.helper = Helper.setup_helper(cfg.login, cfg.domain, cfg.password)
        print('!'*10)

    @pytest.fixture(scope="function")
    def fixture_add_folders(self):
        add_folders(self.helper, cfg.folders)

    @pytest.mark.parametrize(('name'), [
        ('first_test'),
        ('second_test'),
    ])
    def test_folders(self, name):
        from pprint import pprint
        resp = Helper.send_api_request(self.helper, 'folders')
        pprint(resp)