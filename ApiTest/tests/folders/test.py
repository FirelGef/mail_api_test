import pytest

from tools.helper import Helper
from lib.folders_lib import add_folders
from cfg.folders.config import folders_config as cfg

from core import CoreTests


class TestFolders(CoreTests):
    @classmethod
    def setup_class(cls):
        cls.helper = Helper.setup_helper(cfg.login, cfg.domain, cfg.password)

    # TODO add folders without default
    @pytest.fixture(scope="function")
    def fixture_add_folders(self):
        add_folders(self.helper, cfg.folders)

    ###################################

    @pytest.mark.parametrize(('name'), [
        ('first_test'),
        ('second_test'),
    ])
    def test_folders(self, name):
        resp = Helper.send_api_request('folders')

        self.assert_equal(resp['body'], cfg.default_folders, '', True)
