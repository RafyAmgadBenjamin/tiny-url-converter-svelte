<script>
	import Navigation from './Navigation.svelte';
	let name = '';
	let convertedURL = '';
	let ableToConvert = false;
	async function tinyURL(name) {
		//console.log(name);
		const res = await fetch(`http://localhost:8080/urls/add-url/` + name, {
			//		 mode: 'no-cors'  //to handle CORS
		});
		// console.log("response",res.body.getReader().read());
		let data = await res.json();
		convertedURL = 'http://localhost:8080/' + data.tinyUrl;
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
