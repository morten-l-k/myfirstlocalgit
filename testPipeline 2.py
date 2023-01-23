import datapipelines
import unittest

print('------ TEST SUITES ------')
##### UNIT TEST #####
class test_datapipelines_function(unittest.TestCase):
    def test_add_const(self):
        self.assertEqual(datapipelines.AddConst(2).apply(4),6)

    def test_repeater(self):
        self.assertEqual(datapipelines.Repeater(3).apply(3),[3,3,3])
    
    def test_sumNum(self):
        self.assertEqual(datapipelines.SumNum().apply([4,3]),7)

    def test_productNum(self):
        self.assertEqual(datapipelines.ProductNum().apply([3,2,1]),6)

    def test_map(self):
        self.assertEqual(datapipelines.Map(datapipelines.AddConst(4)).apply([3,3]),[7,7])

    def test_pipeline(self):
        self.assertEqual(datapipelines.Pipeline([datapipelines.AddConst(3),
        datapipelines.Repeater(3),datapipelines.ProductNum()]).apply(0),27)

    def test_csv_reader(self):
        tmpDict = datapipelines.CsvReader().apply('critters.csv')
        self.assertEqual(tmpDict[0],{'Name': 'Poppy', 'Colour': 'peru', 'Hit Points': '2'})

    def test_critter_stats(self):
        tmpDict = datapipelines.CsvReader().apply('critters.csv')
        self.assertEqual(datapipelines.CritterStats().apply(tmpDict)['gold'],2)

    def test_show_ascii_bar(self):
        tmpDict = datapipelines.CritterStats().apply(datapipelines.CsvReader().apply('critters.csv'))
        self.assertEqual(datapipelines.ShowAsciiBarchart().apply(tmpDict)['gold'],2)

if __name__ == '__main__':
    unittest.main()

