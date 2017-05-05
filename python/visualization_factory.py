import os
import visualizer_line
import visualizer_bar

class Visualization_Factory:

    '''
    create visualization based on user input
    factory simplifies the arguments of the different visualizers for easy access by the user
    mode = if 1, creates line plot visualization with default settings (window size of 1 minute, 30x10 inches, 100 DPI)
           if 2, creates bar plot visualization with default settings (30x10 inches, 100 DPI)
    khaos = khaos object used for input data
    filename = name of the resulting file
    '''
    def create_visualization(self, mode, khaos, filename):
        dir_name = "./graphs" 
        if mode == 1:
            visualizer = visualizer_line.Visualizer_Line(khaos.get_dataframe())
            visualizer.save_visualization(120, os.path.join(dir_name, filename), 30, 10, 100)
        elif mode == 2:
            visualizer = visualizer_bar.Visualizer_Bar(khaos.get_dataframe())
            visualizer.save_visualization(os.path.join(dir_name, filename), 30, 10, 100)
        else:
            print("not a valid mode")
    
        


    
    
