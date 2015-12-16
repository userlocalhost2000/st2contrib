import time
import datetime

from st2tests.base import BaseActionTestCase

from get_week_boundaries import GetWeekBoundariesTimestampsAction


class GetWeekBoundariesTestCase(BaseActionTestCase):
    def test_run_date_provided(self):
        date = datetime.datetime(2015, 12, 16)
        expected_start_dt = datetime.datetime(2015, 12, 14)
        expected_start_dt = int(time.mktime(expected_start_dt.timetuple()))
        expected_end_dt = datetime.datetime(2015, 12, 20, 23, 59, 59)
        expected_end_dt = int(time.mktime(expected_end_dt.timetuple()))

        actual_start_ts, actual_end_ts = GetWeekBoundariesTimestampsAction().run(date=date)

        self.assertEqual(actual_start_ts, expected_start_dt)
        self.assertEqual(actual_end_ts, expected_end_dt)
