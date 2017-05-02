
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

    def save_to_csv(self, output_filename):
        dir_name = "./csv_files"
        if ".csv" not in output_filename:
            output_filename += ".csv"
        try: 
            self.df.to_csv(os.path.join(dir_name, output_filename))
        except:
            print("There is no dataframe. Create one first")

