import re
from core import CoreTests

ct = CoreTests()
folders_config = type('FoldersConfig', (object,), {})

folders_config.login = login  # '25|19|20|25_12|15|7|9|14_6|12|4|19_20|19'
folders_config.domain = 'mail.ru'
folders_config.password = password  # '11.5|9|11.5|10|25|6|10|24|/2|24.5|1.4|19.5|6.5|/4|14'
folders_config.default_folders = ct.generate_default_folders_template()
folders_config.default_folders[0]['messages_flagged'] = 1
folders_config.default_folders[0]['messages_pinned'] = 0
folders_config.default_folders[0]['messages_snoozed'] = 0
folders_config.default_folders[0]['messages_total'] = 5
folders_config.default_folders[0]['messages_unread'] = 4
