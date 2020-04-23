import re
from prettytable import PrettyTable

def_folders = [{u'id': u'0',
                u'name': u'\u0412\u0445\u043e\u0434\u044f\u0449\u0438\u0435',
                u'system': True,
                u'type': u'inbox'},
               {u'id': u'500000',
                u'name': u'\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0435',
                u'system': True,
                u'only_web': True,
                u'type': u'sent'},
               {u'id': u'500001',
                u'name': u'\u0427\u0435\u0440\u043d\u043e\u0432\u0438\u043a\u0438',
                u'only_web': True,
                u'open': True,
                u'system': True,
                u'type': u'drafts'},
               {u'id': u'950',
                u'name': u'\u0421\u043f\u0430\u043c',
                u'only_web': True,
                u'open': True,
                u'system': True,
                u'type': u'spam'},
               {u'id': u'500002',
                u'name': u'\u041a\u043e\u0440\u0437\u0438\u043d\u0430',
                u'only_web': True,
                u'open': True,
                u'system': True,
                u'type': u'trash'}]

pettytb = []


class CoreTests:
    def assert_reg_dict_equal(self, actual, expected, msg):
        for key in actual.keys():
            assert_result = self.assert_regexp_equal(actual[key], expected[key], msg)
            if not assert_result:
                pettytb.append((f'{key}: {actual[key]}', f'{key}: {expected[key]}'))

    def assert_reg_lists_equal(self, actual_lst, expected_lst, msg):
        for i, actual in enumerate(actual_lst):
            if type(actual) == dict:
                self.assert_reg_dict_equal(actual, expected_lst[i], msg)
            else:
                self.assert_regexp_equal(actual, expected_lst[i], msg)

    def assert_equal(self, actual, expected, msg, regexp=False):

        if regexp:
            if type(actual) == dict:
                self.assert_reg_dict_equal(actual, expected, msg)
            if type(actual) == list:
                self.assert_reg_lists_equal(actual, expected, msg)
            else:
                self.assert_regexp_equal(actual, expected, msg)
        else:
            if actual == expected:
                pettytb.append((f'{actual}', f'{expected}'))

        table = self.generate_petty_table()
        if table:
            print(msg, '\n')
            raise AssertionError(table)

    def assert_regexp_equal(self, actual, expected, msg=''):
        exp_types = [str, int]
        if expected not in exp_types:
            return re.match(str(expected), str(actual))
        else:
            return type(actual) == expected

    def generate_folder_template(self,
                                 folder_id: str,
                                 folder_name: str,
                                 folder_type: str,
                                 **kwargs):
        return [{
            u'archive': kwargs.get('archive', False),
            u'child': kwargs.get('child', False),
            u'children': kwargs.get('children', False),
            u'id': folder_id,
            u'last_visit': kwargs.get('last_visit', int),
            u'messages_flagged': kwargs.get('messages_flagged', 0),
            u'messages_pinned': kwargs.get('messages_pinned', 0),
            u'messages_snoozed': kwargs.get('messages_snoozed', 0),
            u'messages_total': kwargs.get('messages_total', 0),
            u'messages_unread': kwargs.get('messages_unread', 0),
            u'messages_with_attachments': kwargs.get('messages_with_attachments', 0),
            u'name': folder_name,
            u'only_web': kwargs.get('only_web', False),
            u'open': kwargs.get('open', True),
            u'parent': kwargs.get('parent', '-1'),
            u'security': kwargs.get('security', False),
            u'system': kwargs.get('system', False),
            u'type': folder_type
        }]

    def generate_folders_template(self, folders: list):
        """

        :param folders: list of dicts
        [{u'archive': False,
          u'child': False,
          u'children': False,
          u'id': u'0',
          u'last_visit': 1540201948,
          u'messages_flagged': 0,
          u'messages_pinned': 0,
          u'messages_snoozed': 0,
          u'messages_total': 3,
          u'messages_unread': 3,
          u'messages_with_attachments': 0,
          u'name': u'\u0412\u0445\u043e\u0434\u044f\u0449\u0438\u0435',
          u'only_web': False,
          u'open': True,
          u'parent': u'-1',
          u'security': False,
          u'system': True,
          u'type': u'inbox'}]

        """
        folders_template = []
        for folder in folders:
            temp = self.generate_folder_template(folder_id=folder['id'],
                                                 folder_name=folder['name'],
                                                 folder_type=folder['type'],
                                                 **folder)

            folders_template.extend(temp)
        return folders_template

    def generate_default_folders_template(self):
        def_template = self.generate_folders_template(def_folders)

        return def_template

    def generate_petty_table(self):
        if pettytb:
            table = PrettyTable(["actual", "expected"])
            for act, exp in pettytb:
                table.add_row([act, exp])

            return table
