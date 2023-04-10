import json
import unittest
from unittest.mock import MagicMock

import server


class TestServer(unittest.TestCase):

    def setUp(self):
        self.app = server.app.test_client()
        self.app.testing = True

    def test_getRepos_success(self):
        server.requests.get = MagicMock(return_value=MagicMock(json=lambda: [
            {"id": 1, "name": "repo1", "html_url": "https://github.com/user1/repo1", "description": "desc1", "topics": ["topic1", "topic2"]},
            {"id": 2, "name": "repo2", "html_url": "https://github.com/user1/repo2", "description": "desc2", "topics": ["topic3", "topic4"]},
        ]))
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertFalse(data["error"])
        self.assertEqual(len(data["projects"]), 2)
        self.assertEqual(data["projects"][0]["id"], 1)
        self.assertEqual(data["projects"][0]["name"], "repo1")
        self.assertEqual(data["projects"][0]["url"], "https://github.com/user1/repo1")
        self.assertEqual(data["projects"][0]["description"], "desc1")
        self.assertEqual(data["projects"][0]["topics"], ["topic1", "topic2"])
        self.assertEqual(data["projects"][1]["id"], 2)
        self.assertEqual(data["projects"][1]["name"], "repo2")
        self.assertEqual(data["projects"][1]["url"], "https://github.com/user1/repo2")
        self.assertEqual(data["projects"][1]["description"], "desc2")
        self.assertEqual(data["projects"][1]["topics"], ["topic3", "topic4"])

    def test_getRepos_error(self):
        server.requests.get = MagicMock(side_effect=Exception("Something went wrong"))
        response = self.app.get('/')
        self.assertEqual(response.status_code, 500)
        data = json.loads(response.data)
        self.assertTrue(data["error"])
        self.assertEqual(data["message"], "Something went wrong")


if __name__ == '__main__':
    unittest.main()