import unittest
from download_remaining_time_estimate import RemainingTime

class TestDownloadRemainingTime(unittest.TestCase):

    # def setUp(self):
    #     problem = RemainingTime

    def test_downloaded_down(self):
        ans = RemainingTime(100, [25,25,30,20],2)
        self.assertEquals(ans.solution(), 0)

    def test_download_rate(self):
        ans = RemainingTime(100, [10,6,6,8] ,2)
        self.assertTrue(ans.solution(), 10)

    def test_z_observations_fewer(self):
        ans = RemainingTime(100, [10,10,10] ,4)
        self.assertEqual(ans.solution(), 7)