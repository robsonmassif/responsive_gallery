# responsive_gallery
Test app for making a responsive web app with polymer, app engine endpoints and cloudstore to make a responsive web app that displays a gallery

This is basically a simple example of how to make a simple responsive javascript driven front-end talk to a backend using Google Cloud Platform APIs, that are written in Python for the moment.

## Installing
### Dependencies

  1. [Google App Engine Python SDK](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)
  2. Node.Js especially Node Package Manager [NPM](http://blog.npmjs.org/post/85484771375/how-to-install-npm). This is basically just to install Bower in order to manage Polymer packages
  3. A Google Cloud Platform account and a "Project ID"

### Installing the project

  1. Clone the repo
  2. ```npm install -g bower``` To install bower, the thing that manages all the Polymer dependencies installation
  3. ```bower install``` This will check the ```bower.json``` file and install all the required Polymer dependencies
  4. Paste your Google Cloud Platform "Project ID" in the ```application: ``` field in the ```app.yaml```
  5. Enable Datastore on your Google Cloud Platform account
  5. Navigate to the top level folder in the repo and run the app with the command ``` dev_appserver.py .```
  6. Load ```http://localhost:8080/``` 

