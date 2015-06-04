import unittest
import copy
import time
import datetime
import random

import timeUUID

class TimeUUIDTest(unittest.TestCase):
    
    def testInit(self):
        testObj = timeUUID.TimeUUID()
        self.assertEqual(testObj.__class__, timeUUID.TimeUUID)
        
        # test intializing with timestamp
        timestamp = time.time()
        testObj2 = timeUUID.TimeUUID(timestamp=timestamp)

    def testStr(self):
        testObj = timeUUID.TimeUUID()
        self.assertEqual(len(str(testObj)), 36)
        
    def testEQ(self):
        testObj = timeUUID.TimeUUID()
        testObj2 = copy.deepcopy(testObj)
        testObj3 = timeUUID.TimeUUID()
        
        self.assertTrue(testObj == testObj2)
        self.assertFalse(testObj == testObj3)
        
    def testNE(self):
        testObj = timeUUID.TimeUUID()
        testObj2 = timeUUID.TimeUUID()
        
        self.assertTrue(testObj < testObj2)
        self.assertFalse(testObj2 < testObj)
        
    def testInitFromHex(self):
        testObj = timeUUID.TimeUUID()
        testObjHex = timeUUID.TimeUUID(str(testObj))
        self.assertTrue(testObj == testObjHex)
                
        with self.assertRaises(TypeError):
            testObjHex2 = timeUUID.TimeUUID(str(testObj), timestamp=testObj.timestamp)

    def testGT(self):
        testObj = timeUUID.TimeUUID()
        testObj2 = timeUUID.TimeUUID()
        
        self.assertTrue(testObj2 > testObj)
        self.assertFalse(testObj > testObj2)
    
    def testLT(self):
        testObj = timeUUID.TimeUUID()
        testObj2 = timeUUID.TimeUUID()
        
        self.assertTrue(testObj < testObj2)
        self.assertFalse(testObj2 < testObj)
        
    def testGE(self):
        testObj = timeUUID.TimeUUID()
        testObj2 = copy.deepcopy(testObj)
        testObj3 = timeUUID.TimeUUID()
        
        self.assertTrue(testObj >= testObj2)
        self.assertTrue(testObj3 >= testObj)
        self.assertFalse(testObj >= testObj3)
        
    def testLE(self):
        testObj = timeUUID.TimeUUID()
        testObj2 = copy.deepcopy(testObj)
        testObj3 = timeUUID.TimeUUID()
        
        self.assertTrue(testObj <= testObj2)
        self.assertTrue(testObj <= testObj3)
        self.assertFalse(testObj3 <= testObj)
        
    def testInt(self):
        testObj = timeUUID.TimeUUID()
        self.assertTrue(isinstance(int(testObj), int))

    def testSetAttr(self):
        testObj = timeUUID.TimeUUID()
        
        with self.assertRaises(TypeError):
            testObj.int = 1
            
        with self.assertRaises(TypeError):
            testObj.timestamp = 1

    def testTime(self):
        timestamp = time.time()
        testObj = timeUUID.TimeUUID()
        testObj2 = timeUUID.TimeUUID(timestamp = timestamp)

        # Equal with 4 decimal places
        self.assertAlmostEqual(testObj.timestamp, timestamp, places=4)
        # Due to rounding error this could be off by 1 decimal place
        self.assertAlmostEqual(testObj.timestamp, timestamp, places=1)
        
    def testDate(self):
        testObj = timeUUID.TimeUUID()
        current = datetime.datetime.now()
        
        self.assertEqual(current.year, testObj.datetime.year)
        self.assertEqual(current.month, testObj.datetime.month)
        self.assertEqual(current.day, testObj.datetime.day)
        self.assertEqual(current.hour, testObj.datetime.hour)
        self.assertEqual(current.minute, testObj.datetime.minute)
        self.assertEqual(current.second, testObj.datetime.second)
        
    def testOrdering(self):
        ids = []
        
        n = 1000
        
        # test with general dates
        for i in range(n):
            date = datetime.datetime(random.randrange(2000, 2030), random.randrange(1, 13), random.randrange(1, 29), random.randrange(24), random.randrange(60))
            ids.append(timeUUID.TimeUUID(timestamp = date.timestamp()))
        
        sorted_ids = sorted(ids, reverse=True)

        for i in range(n):
            self.assertTrue(all(sorted_ids[i] >= other for other in sorted_ids[i+1:]))
            
        # make sure that the order stays the same
        sorted_ids2 = sorted(ids, reverse=True)
        self.assertEqual(sorted_ids, sorted_ids2)
        
    def testCollisions(self):
        ids = {}
        
        n = 10000
        
        for i in range(n):
            id = timeUUID.TimeUUID()
            self.assertFalse(str(id) in ids)
            ids[str(id)] = True
        
        self.assertEqual(len(ids.keys()), n)
        
            

        
