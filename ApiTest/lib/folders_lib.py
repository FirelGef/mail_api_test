from tools.helper import Helper

def add_folders(helper, folder_params):

    response = Helper.send_api_request(helper, 'folders/add', folder=folder_params)

    if response['status'] != 200:
        raise RuntimeError('Failed to get {0}. {0} response: {1}'.format('folders/add', response))

    return response

