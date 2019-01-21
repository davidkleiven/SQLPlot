import unittest
import dataset
import os
from sqlplot import SQLPlot

DB_NAME = "somedatabase.db"
TABLE = "exampletable"
PREFIX = "sqlite:///"

def db_url():
    return PREFIX + DB_NAME

def create_ex_db():
    db = dataset.connect(db_url())

    x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    y = [0.6, -0.2, 0.8, 0.9, 1.0, 10.0]
    tbl = db[TABLE]
    for valx, valy in zip(x, y):
        tbl.insert({"x": valx, "y": valy})

class TestSQLPlot(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        create_ex_db()

    def test_simple_plot(self):
        plotter = SQLPlot(db_url())

        no_exceptions_thrown = True
        msg = ""
        try:
            sql = "select x, y from {}".format(TABLE)
            plotter.plot_query(sql)
        except Exception as exc:
            msg = "{}_{}".format(type(exc).__name__, str(exc))
            no_exceptions_thrown = False
        self.assertTrue(no_exceptions_thrown, msg=msg)

    def doCleanups(self):
        os.remove(DB_NAME)
        unittest.TestCase.doCleanups(self)

if __name__ == "__main__":
    unittest.main()

