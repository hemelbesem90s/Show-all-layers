import inkex
import datetime

class ShowAllLayers(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.log_file = 'extension_log.txt'
        self.enable_logging = False

    def effect(self):
        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write(f"--- ShowAllLayers ---\n")
                f.write(f"{datetime.datetime.now()}\n")

        # Select layers using XPath
        layers = self.svg.xpath('//svg:g[@inkscape:groupmode="layer"]')

        # Make all layers visible
        for layer in layers:
            layer.set('style', "display:inline;")
            self.print_to_log(f"Showed layer: {layer.get(inkex.addNS('label', 'inkscape'))}")

        # Update the SVG document
        self.document.write(self.options.input_file)

        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write('\n\n')

    def print_to_log(self, message):
        """Prints a message to the log file if logging is enabled."""
        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write(message + '\n')

if __name__ == '__main__':
    ShowAllLayers().run()