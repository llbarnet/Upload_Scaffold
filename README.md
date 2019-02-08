# Upload Scaffold
This is a quick boilerplate code to allow adding images to your static folder.

# Installation
To properly run this on your local machine you will need **python** and **flask**.
The site will run on localhost:5000 unless changed:
  `app.run(host='0.0.0.0', port=5000)`

# Features
This code will allow for whatever extensions supplied in  `ALLOWED_EXTENSIONS`
and can be altered to fit personal needs.

The app will flash to confirm successful uploads, missing filetypes, or unsupported filetypes.

Change the directed upload folder where
`UPLOAD_FOLDER = os.path.basename('static')`

## Additional Uses
If connected with a database each filename derived from the upload can be saved to the database and called upon later to display the uploaded images. This can be used to support the addition of images in a personal blog or site that needs updating from web-side application. 
