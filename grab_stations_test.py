#!/usr/bin/env python3.3
import unittest
import grab_stations

class TestParsing(unittest.TestCase):

    def test_parse_line(self):
        line = ' 8   KVYS PERU                 IL   41.35N    89.15W'
        stn, lat, lon = grab_stations.parse_station_line(line)
        self.assertEqual(['KVYS', 41.35, -89.15], [stn, lat, lon])
    
    def test_extract_illinois_section(self):
        line = 'PRE This is the test IL result.  PRE'
        test_result = grab_stations.extract_illinois_section(line)
        self.assertEqual('This is the test IL result.',test_result)
    
#    def 
        





if __name__ == '__main__':
    unittest.main()
