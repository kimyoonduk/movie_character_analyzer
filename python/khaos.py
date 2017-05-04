
import os
import pandas as pd

class Khaos:
    
    def __init__(self):
        self.aos = { }

    # placeholder
    def calculate_khaos(self):
        return 0

    def zero_aos(self, actor):
        self.aos[actor].append(0)
    
    def mark_aos(self, actor, frame_index):
        self.aos[actor][frame_index] = 1

    def get_aos(self):
        return self.aos

    def make_dataframe(self):
        self.df = pd.DataFrame(self.aos)
        return self.df

    def get_dataframe(self):
        try:
            return self.df
        except:
            print("There is no dataframe. Create one first.")
    
    def get_df_from_csv(self, filepath):
        temp_df = pd.read_csv(filepath)
        del temp_df['Unnamed: 0']
        self.df = temp_df

    def save_to_csv(self, output_filename):
        dir_name = "./csv_files"
        if ".csv" not in output_filename:
            output_filename += ".csv"
        try: 
            self.df.to_csv(os.path.join(dir_name, output_filename))
        except:
            print("There is no dataframe. Create one first.")

