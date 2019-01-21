import dataset
from matplotlib import pyplot as plt

class SQLPlot(object):
    def __init__(self, db_name):
        self.db = dataset.connect(db_name)

    def plot(self, x, y, ax=None, marker="o", 
             xlabel="", ylabel=""):
        """Plots x and y.
        
        :param list x: List with x values
        :param list y: List with y values
        :param Axes ax: If given the curve will
            be plotted using the passed axes object
        :param str marker: Marker for the points
        :param str xlabel: xlabel
        :param str ylabel: ylabel
        """
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)

        # We sort according to x
        sorted_on_x = sorted(zip(x, y))
        x = [item[0] for item in sorted_on_x]
        y = [item[1] for item in sorted_on_x]
        ax.plot(x, y, marker=marker)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

    def plot_query(self, sql):
        """Creates a plot of the query.
        
        :param str sql: SQL query
        """
        x = []
        y = []
        xlabel = ""
        ylabel = ""
        for row in self.db.query(sql):
            keys = list(row.keys())

            if len(keys) < 2:
                raise ValueError("Query needs to result in at least "
                                 "two columns being returned! Got {}"
                                 "".format(len(keys)))
            xlabel = keys[0]
            ylabel = keys[1]
            x.append(row[keys[0]])
            y.append(row(keys[1]))
    
        self.plot(x, y, xlabel=xlabel, ylabel=ylabel)


    