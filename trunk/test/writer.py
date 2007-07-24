import util
import unittest
import pymarc
import re
import os

class MARCWriterTest(unittest.TestCase):

    def test_write(self):

        # write a record off to a file
        writer = pymarc.MARCWriter(file('test/writer-test.dat','w'))
        record = pymarc.Record()
        field = pymarc.Field('245', ['0','0'], ['a', 'foo'])
        record.addField(field)
        writer.write(record)
        writer.close()

        # read it back in
        reader = pymarc.MARCReader(file('test/writer-test.dat'))
        record = reader.next()

        # remove it
        os.remove('test/writer-test.dat')

def suite():
    suite = unittest.makeSuite(MARCWriterTest, 'test')
    return suite

if __name__ == "__main__":
    unittest.main()
