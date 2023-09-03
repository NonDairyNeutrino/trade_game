from planet import Planet
import ui

new_planets = [Planet() for i in range(3)]

ui.probe_prompt(new_planets)