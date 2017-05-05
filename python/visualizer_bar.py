import pandas as pd
import matplotlib.animation
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer_Bar:

    def __init__(self, df):
        self.df = df
        self.num_characters = len(self.df.columns)
        sns.set_palette("Set2", self.num_characters)


    def save_visualization(self, savepath, width, height, dpi_val):
        max_appearance = self.get_max_appear()

        char_dict = {}
        for column in self.df:
            char_dict[column] = self.df[column].sum()

        fig, ax = plt.subplots()
        fig.set_size_inches(width, height)
        ax.set_ylim([0,max_appearance + 20])

        plt.xlabel('Characters')
        plt.ylabel('Appearance on Screen')
        plt.title('Character Appearance Over Time')

        bars = ax.bar(range(len(char_dict)), char_dict.values(), align='center')
        plt.xticks(range(len(char_dict)), char_dict.keys())

        fig.savefig(savepath, dpi=dpi_val)

    def get_max_appear(self):
        appear_sum = []
        for column in self.df:
            appear_sum.append(self.df[column].sum())
        return max(appear_sum)

    '''
    helper method to remove all columns from the dataframe except the original information
     
    '''
    def delete_new_columns(self, num_characters):
        for i in range (len(self.df.columns) - num_characters):
            self.df.drop(self.df.columns[[num_characters]], axis=1, inplace=True) 

if __name__ == "__main__":
    print("starting main...")
    new_df = pd.read_csv('csv_files/crazy.csv')
    del new_df['Unnamed: 0']
    new_vis = Visualizer_Bar(new_df)

    new_vis.save_visualization("bar_crazystupidlove.png", 20, 10, 100)


