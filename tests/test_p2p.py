import unittest
from hips.client import Client
from hips.server import Server

# TODO
class TestPeer2Peer(unittest.TestCase):
    def setUp(self):
        self.client = None
        self.server = None