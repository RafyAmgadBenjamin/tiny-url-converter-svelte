<script>
	let name = '';
	let convertedURL = '';
	function tinyURL(name) {
		console.log(name);
		convertedURL = name + 'testing';
	}
</script>

<div>
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
					<b>Long URL:</b> <p>{name}</p>
				</div>
				<!--[Short-Url]-->
				<div>
					<b>Short URL:</b> <p>{convertedURL}</p>
				</div>
			{/if}

		</div>
	</div>
</div>
