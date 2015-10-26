#Jelma'Bell

This is a simple project i use to teach the basics of the MVC in pyqt.
The resulting app is a simple csv editor.

##Steps

An explanation of the steps follows

### SHA: 22b4b069c96677c87ece3ecaefebda1fa8036714

Till this step, the app is very basic, it just shows

- How to make a basic pyqt app (GelmaGui) and how to load a .ui file, using it as a gui
- How to start a pyqt app (tail -n 20 of gelma.py)
- There is the skeleton of a model calss, just showing the basic metohd to implement
to have it feed data to the view

### SHA: d871b00d26a94d3c509322a664baa4e56f9aef08

The app start to load and save data on csv (shows how the data retrieving methods are implemented)

### SHA: 55abe838e9eb2d8032b20c1d194a99b259541fb2

The diff contains the signals to launch when the modelneeds the view to refresh, a.k.a. how to refresh the view 
to match the model.

### SHA: 50b332e922ab77c3ab933bfd0dcafe8b62440bb6

The app handles button press events the "pythonic" way, and clicks on the table grid

### SHA: 3cf8214cc58e2bfd7146f64886312658fd666c4f

these commits shows how make a proper app that installs in the python environment
