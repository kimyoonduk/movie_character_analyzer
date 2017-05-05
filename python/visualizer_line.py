import pandas as pd
import matplotlib.animation
import matplotlib.pyplot as plt
import seaborn as sns


class Visualizer_Line:

    def __init__(self, df):
        self.df = df
        self.appear_list = []
        self.num_characters = len(self.df.columns)
        sns.set_palette("Set2", self.num_characters)


    def save_visualization(self, window, savepath, width, height, dpi_val):
        self.appear_list = []
        self.create_count_column(window)
        self.df['minutes'] = self.df.index.values / 120
        self.df.set_index('minutes')
        fig = plt.gcf()
        fig.set_size_inches(width, height)

        for column in self.df:
            if ('count_' in column):
                self.df[column].plot(label=column[6:])

        legend = plt.legend(loc='best')
        plt.xlabel('Time (in half seconds)')
        plt.ylabel('Appearance in the last ' + str(window) + ' frames')
        plt.title('Appearance over time')
        fig.savefig(savepath, dpi=dpi_val)


    def create_count_column(self, window):
        global appear_list
        for column in self.df:
            appear_list = []
            count_column = "count_" + column
            self.df[count_column] = self.df.apply(lambda row: self.get_frame_count(row, column, window), axis = 1)

    '''
    gets the number of character appearances in the last n frames
    row = argument for the lambda function
    charname = name of the character
    window = number of last n frames
    '''
    def get_frame_count(self, row, charname, window):
        global appear_list
        if (len(appear_list) >= window):
            appear_list.pop(0)
        appear_list.append(row[charname])
        return sum(appear_list)

    '''
    helper method to remove all columns from the dataframe except the original information
     
    '''
    def delete_new_columns(self, num_characters):
        for i in range (len(self.df.columns) - num_characters):
            self.df.drop(self.df.columns[[num_characters]], axis=1, inplace=True) 

if __name__ == "__main__":
    print("starting main...")
    new_df = pd.read_csv('basterds1.csv')
    del new_df['Unnamed: 0']
    new_vis = Visualizer_Line(new_df)

    new_vis.save_visualization(100, "test_output.png", 30, 10, 100)
