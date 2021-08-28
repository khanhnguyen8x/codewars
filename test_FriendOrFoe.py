from unittest import TestCase
from FriendOrFoe import friend

class Test(TestCase):
    def test_friend(self):
        self.assertEqual(friend(["Ryan", "Kieran", "Jason", "Yous"]), ['Ryan', 'Yous'])
        self.assertEqual(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ['Ryan'])
        self.assertEqual(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])

