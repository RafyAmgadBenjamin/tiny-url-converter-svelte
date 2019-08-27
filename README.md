

# svelte app

This is a project template for [Svelte](https://svelte.dev) apps. It lives at https://github.com/sveltejs/template.

To create a new project based on this template using [degit](https://github.com/Rich-Harris/degit):

```bash
npx degit sveltejs/template svelte-app
cd svelte-app
```

*Note that you will need to have [Node.js](https://nodejs.org) installed.*


## Get started

Install the dependencies...

```bash
cd svelte-app
npm install
```

...then start [Rollup](https://rollupjs.org):

```bash
npm run dev
```

Navigate to [localhost:5000](http://localhost:5000). You should see your app running. Edit a component file in `src`, save it, and reload the page to see your changes.

## Working on front-end
* Add all the front-end libraries <b> example</b> ```Bootsrap and Font awesome``` in ```/public/index.html```

* Create navigation component <b>example</b> ```Navigation.svelte``` and import this component in ```App.svelte``` <b>example</b> ```import Navigation from './Navigation.svelte';```

* Create your html elements in ```App.svelte```

## Working on back-end
* Create python file <b>example</b> ```UrlApi.py``` which will contain the code to handle the URLs

* Install bottle Web FrameWork ```pip install bottle```

* Import the server in the python file ```from bottle import route``` then create your APIs to handle the comming requests

* Create random number genrator which will create the tiny URL

* Install Redis database ```pip install redis```

* Import Redis into the python file ```import redis```,Create a Redis client with your configuratins and use Redis commands

* Store the data in Redis database 



## Deploying to the web

### With [now](https://zeit.co/now)

Install `now` if you haven't already:

```bash
npm install -g now
```

Then, from within your project folder:

```bash
cd public
now
```

As an alternative, use the [Now desktop client](https://zeit.co/download) and simply drag the unzipped project folder to the taskbar icon.


