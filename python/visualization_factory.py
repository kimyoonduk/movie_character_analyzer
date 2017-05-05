import os
import visualizer_line

class Visualization_Factory:

    def create_visualization(self, mode, khaos, filename):
        dir_name = "./graphs" 
        if mode == 1:
            visualizer = visualizer_line.Visualizer_Line(khaos.get_dataframe())
        elif mode == 2:
            visualizer = visualizer_line.Visualizer_animation()
        else:
            print("not a valid mode")
        visualizer.save_visualization(120, os.path.join(dir_name, filename), 30, 10, 100)
    
        


    
    
