import pytest

from tools.helper import Helper
from cfg.folders.config import folders_config as cfg

from core import CoreTests

class TestFolders(CoreTests):
    @classmethod
    def setup_class(cls):
        cls.helper = Helper.setup_helper(cfg.login, cfg.domain, cfg.password)
        print('!'*10)

    @pytest.fixture(scope="function")
    def fixture_add_folders(self):
        pass

    @pytest.mark.parametrize(('name'), [
        ('first_test'),
        ('second_test'),
    ])
    def test_folders(self, name):
        resp = Helper.send_api_request(self.helper, 'folders')
        print(resp)