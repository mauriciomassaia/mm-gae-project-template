## Project template with:

[Google Appengine][gae-link]

[Google Web Starter kit][gwsk-link]

[gae-link]: https://developers.google.com/appengine/docs/python
[gwsk-link]:https://developers.google.com/web/starter-kit/
### Install the npm dependencies

```
$ npm install 
```

### to run the debug version
Update the appengine/app.yaml file to:

	includes:
	- debug.yaml
	#- build.yaml

run this command to compile sass and lint the javascript.
```
$ gulp watch
```

### to build the optimized version
Update the appengine/app.yaml file to:

	includes:
	#- debug.yaml
	- build.yaml

Run this command to compile Sass and compress front-end files:

```
$ gulp
```

Then you can deploy the optimized vertion to appengine.