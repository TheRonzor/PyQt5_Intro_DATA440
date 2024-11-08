### Example GUIs using PyQt5

Created for students of DATA 440: Automation & Workflows (Fall 2024)

Files included:

- `simple.py`: Script to run a simple app which allows the user to enter their name and says hello to them.

- `figure_with_data.py`: (Will be written in class). An app containing a window with a figure and some buttons to generate/save/load data and figures.
 
---
`src/`
 - `globals.py`: Imports, constants, and helper functions shared across modules.

 - `my_analysis.py`: Contains a class for random data generation. Included to emphasize that code for data manipulation/analysis should be separate from code for making plots or front-end design. 

 - `my_plots.py`: Contains a class to create scatter plots. Included to emphasize that code for working with figures should be separate from code fpr data manipulation/analysis or front-end design.

 - `qt_components.py`: (Will be written in class). Code for our custom UI elements designed in PyQt5.