<script>
	import { openDB, deleteDB, wrap, unwrap } from 'idb';
	import Navigation from './Navigation.svelte';
	let name = '';
	let convertedURL = '';
	let ableToConvert = false;
	function tinyURL(name) {
		console.log(name);
		convertedURL = name + 'testing';
	}
	function copyToClipboard() {
		var range = document.createRange();
		range.selectNode(document.getElementById('tinyURL'));
		window.getSelection().removeAllRanges(); // clear current selection
		window.getSelection().addRange(range); // to select text
		document.execCommand('copy');
		window.getSelection().removeAllRanges(); // to deselect
	}
	$: if (name == '') {
		convertedURL = '';
	}
	//Database

	async function addNewUrl(newTinyUrl, newOriginalUrl) {
		const db = await openDB('UrlData', 1, {
			upgrade(db) {
				//console.log(' I have enter upgrade');
				// Create a store of objects
				const store = db.createObjectStore('urls', {
					// The 'id' property of the object will be the key.
					// keyPath: 'tinyUrl',
					keyPath: 'id',
					// If it isn't explicitly set, create a value by auto incrementing.
					autoIncrement: true,
				});
				// Create an index on the 'date' property of the objects.
				store.createIndex('id', 'id');
			},
		});

		// Add an article:
		const tx = db.transaction('urls', 'readwrite');
		await tx.store.add({
			tinyUrl: newTinyUrl,
			originalUrl: newOriginalUrl,
		});
		await tx.done;

		const value = await db.getFromIndex('urls', 'id', 1);
		console.log(value);
	}

	addNewUrl('434fds', 'www.google.com')
		.then(res => {
			console.log('success', res);
		})
		.catch(e => console.log('fail', e));
	addNewUrl('234dsf4', 'www.facebook.com')
		.then(res => {
			console.log('success', res);
		})
		.catch(e => console.log('fail', e));
	
</script>

<div>
	<Navigation />
</div>

<div class="container ">
	<div class="mt-3">
		<h1>Long URL converter</h1>
	</div>
	<div class="row">
		<div class="col-sm-12">

			<!--[Long-URL-Input]-->
			<div class="d-flex justify-content-start">
				<div>
					<input bind:value={name} />
				</div>

				<!--[Convert-BTN]-->
				<div>
					<button class="btn btn-primary ml-2" on:click={() => tinyURL(name)}>
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
								Copy
							</button>
						</div>
					</div>
				</div>
			{/if}

		</div>
	</div>
</div>
