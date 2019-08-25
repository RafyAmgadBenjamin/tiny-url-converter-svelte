<script>
	import Navigation from './Navigation.svelte';
	let name = '';
	let convertedURL = '';
	function tinyURL(name) {
		console.log(name);
		convertedURL = name + 'testing';
	}
	function copyToClipboard() {
		// var copyText = document.getElementById('tinyURL');
		// console.write(copyText)
		// // copyText.select();
		// copyText.setSelectionRange(0, 99999);
		// // copyText.select()

		// document.execCommand('copy');
		// alert('Copied the text: ' + copyText.value);
		var range = document.createRange();
                    range.selectNode(document.getElementById("tinyURL"));
                    window.getSelection().removeAllRanges(); // clear current selection
                    window.getSelection().addRange(range); // to select text
                    document.execCommand("copy");
                    window.getSelection().removeAllRanges();// to deselect
	}
</script>

<div>
	<Navigation />
</div>
<div class="mt-3">
	<h1>Long URL converter</h1>
</div>
<div class="container mt-5">
	<div class="row">
		<!--[Tasks-Data]-->
		<div class="col-sm-12">

			<input bind:value={name} />

			<!--[Convert-BTN]-->
			<button on:click={() => tinyURL(name)}>Convert</button>
			{#if convertedURL != ''}
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
			{/if}

		</div>
	</div>
</div>
