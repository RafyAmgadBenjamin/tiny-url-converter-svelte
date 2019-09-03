This is a tool which is used to convert the long URL into a tiny professional one to be used in other websites.

# Features
* Tiny URL generation.
* Redirection to the original URL when the tiny one is used.


# svelte app

This is a project template for [Svelte](https://svelte.dev) apps. It lives at https://github.com/sveltejs/template.

To create a new project based on this template using [degit](https://github.com/Rich-Harris/degit):

```bash
npx degit sveltejs/template svelte-app
cd svelte-app
```

*Note that you will need to have [Node.js](https://nodejs.org) installed.*


# Get started

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

## project structure 
```
.
├── actors
│   └── url.py
├── back-end
│   ├── UrlApi.py
│   └── views
│       └── 404.tpl
├── front-end
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   ├── favicon.png
│   │   ├── global.css
│   │   └── index.html
│   ├── rollup.config.js
│   └── src
│       ├── App.svelte
│       ├── main.js
│       └── Navigation.svelte
├── models
│   └── threefold_grid_url.toml
├── package.py
├── README.md
└── tree

7 directories, 16 files
```

## Working on front-end
* Add all the front-end libraries <b> example</b> ```Bootsrap and Font awesome``` in ```/public/index.html```

* Create navigation component <b>example</b> ```front-end/src/Navigation.svelte``` and import this component in ```front-end/src/App.svelte``` <b>example</b> ```import Navigation from './Navigation.svelte';```
to use this component ```<Navigation />```

* Create your html elements and logic in ```front-end/src/App.svelte```

* Create the layout
```html
<div class="container ">
	<div class="mt-3">
		<h1>Long URL converter</h1>
	</div>
	<div class="row">
		<div class="col-sm-12">
			<!--[Long-URL]-->
			<div class="row">
				<!--[Long-URL-Input]-->
				<div class="col-sm-10">
					<input class="w-100" bind:value={name} />
				</div>

				<!--[Convert-BTN]-->
				<div class="col-sm-2 mt-2 mt-sm-0">
					<button class="btn btn-primary" on:click={() => tinyURL(name)}>
						Convert
					</button>
				</div>

			</div>
			{#if convertedURL != '' && name != ''}
				<div class="mt-4">
					<!--[Long-url]-->
					<div>
						<b>Long URL:</b>
						<p>{name}</p>
					</div>
					<!--[Short-Url]-->
					<div class="d-flex justify-content-start">
						<!--[Short-Url-Text]-->
						<div>
							<b>Short URL:</b>
							<p id="tinyURL">{convertedURL}</p>
						</div>
						<!--[Copy-BTN]-->
						<div class="ml-3">
							<button class="btn btn-light" on:click={() => copyToClipboard()}>
								<i class="far fa-copy"></i>
							</button>
						</div>
					</div>
				</div>
			{/if}
		</div>
	</div>
</div>
``` 
* Fetch data from the API
```javascript
async function tinyURL(name) {
		const res = await fetch(`http://localhost:8080/urls/add-url/` + name, {
		});
		let data = await res.json();
		convertedURL = 'http://localhost:8080/' + data.tinyUrl;
	}
```

## Working on back-end
* Create python file <b>example</b> ```back-end/UrlApi.py``` which will contain the code to handle the APIs

* Install bottle Web FrameWork ```pip install bottle```

* Import the server in the python file ```from bottle import route``` then create your APIs to handle the comming requests 
```python
@get('/urls/add-url/<originalUrl:path>')
def add_Url(originalUrl):
    generatedVal = str(generate_random_no())
    add_url_redis(tinyUrl=generatedVal, originalUrl=originalUrl)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({'tinyUrl': generatedVal})
```

* Create random number genrator which will create the tiny URL ```import random```  and <b>example</b> for the logic 
```python
def generate_random_no():
    random.seed(a=None)
    return randint(0, 1000000)  # randint is inclusive at both ends
```

* Install Redis in your system 
``` bash
    sudo apt update
    sudo apt install redis-server
```

* Install Redis database in your project ```pip install redis```
we will store the <b>Tiny URL</b> (which is randomly generated) and the <b>Original URL </b>

* Import Redis into the python file ```import redis```,Create a Redis client with your configurations 
```python
redis_host = "localhost"
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(host=redis_host, port=redis_port,
                          password=redis_password, decode_responses=True)
```
 * use Redis commands to store and get the data in Redis database ```r.set(tinyUrl, originalUrl)``` and ```r.get(tinyUrl)```

## Use Gedis from Jumpscale
* Create actors ```actors/url.py``` 
```python
class url():
    def __init__(self, *args, **kwarsg):
        self.bcdb = j.data.bcdb.get("url_test")
        self.model = self.bcdb.model_get(url="threefold.grid.url")

    def ping(self):
        True
``` 
* Create modeles ```models/threefold_grid_url.toml```
    ```python
    @url = jumpscale.bcdb.model.url_model
    tinyUrl* = "" (S)
    originalUrl = "" (S)
    ```


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


