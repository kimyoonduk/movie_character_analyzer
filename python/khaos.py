
import os
import pandas as pd
class Khaos:

    '''
    constructor
    initializes a dictionary that contains each character and the list of appearances
    '''
    def __init__(self):
        self.aos = { } 

    #placeholder: functino for future expansion 
    def calculate_khaos(self):
        return 0

    '''
    helper method to edit actor appearance list
    '''
    def zero_aos(self, actor):
        self.aos[actor].append(0)

    '''
    helper method to mark actor appearance
    '''
    def mark_aos(self, actor, frame_index):
        self.aos[actor][frame_index] = 1

    '''
    getter for aos dictionary
    '''
    def get_aos(self):
        return self.aos

    '''
    creates pandas dataframe from the aos dictionary
    '''
    def make_dataframe(self):
        self.df = pd.DataFrame(self.aos)
        return self.df

    '''
    return dataframe if it exists
    '''
    def get_dataframe(self):
        try:
            return self.df
        except:
            print("There is no dataframe. Create one first.")
   
    '''
    reads and saves a dataframe from an existing csv file
    '''
    def get_df_from_csv(self, filepath):
        dir_name = "./csv_files"
        temp_df = pd.read_csv(os.path.join(dir_name,filepath))
        del temp_df['Unnamed: 0']
        self.df = temp_df

    '''
    save the pandas dataframe to csv file
    '''
    def save_to_csv(self, output_filename):
        dir_name = "./csv_files"
        if ".csv" not in output_filename:
            output_filename += ".csv"
        try: 
            self.df.to_csv(os.path.join(dir_name, output_filename))
        except:
            print("There is no dataframe. Create one first.")

