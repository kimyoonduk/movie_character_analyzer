import os
import visualizer_line
import visualizer_bar

class Visualization_Factory:

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
    
        


    
    
