import requests
import sys

sys.path.append('../cfg')

from cfg.prod_config import *

def helper(endpoint):
    with requests.Session() as session:
        session.get('')

