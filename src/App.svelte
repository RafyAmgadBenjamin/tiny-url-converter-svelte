<script>
	import Navigation from './Navigation.svelte';
	let name = '';
	let convertedURL = '';
	let ableToConvert = false;
	async function tinyURL(name) {
		//console.log(name);
		const res = await fetch(`http://localhost:8080/urls/add-url/`+name,{
			 mode: 'no-cors'  //to handle CORS
		});
		console.log(res)
		convertedURL = res;
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

	//Call APIs
	//Get the original url
	// onMount(async () => {
	// 	const res = await fetch(`http://localhost:8080/urls/add-url/`+name);
	// 	convertedURL = res;
	// });
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
