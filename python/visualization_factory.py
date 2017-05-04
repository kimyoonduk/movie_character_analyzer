class VisualizationFactory:

    def create_visualizer(self, type, khaos, filename):
        if type == 1:
            visualizer = Visualizer_line()
        if type == 2:
            visualizer = Visualizer_animation()
        else:
            print("not a valid type")
        return visualizer


    
    
