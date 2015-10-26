#Jelma'Bell

This is a simple project i use to teach the basics of the MVC in pyqt.
The resulting app is a simple csv editor.

##Steps

An explanation of the steps follows

### SHA: 22b4b06

Till this step, the app is very basic, it just shows

- How to make a basic pyqt app (GelmaGui) and how to load a .ui file, using it as a gui
- How to start a pyqt app (tail -n 20 of gelma.py)
- There is the skeleton of a model calss, just showing the basic metohd to implement
to have it feed data to the view

### SHA: d871b00

The app start to load and save data on csv (shows how the data retrieving methods are implemented)

### SHA: 55abe83

The diff contains the signals to launch when the modelneeds the view to refresh, a.k.a. how to refresh the view 
to match the model.

### SHA: 50b332e

The app handles button press events the "pythonic" way, and clicks on the table grid

### SHA: 3cf8214

these commits shows how make a proper app that installs in the python environment
