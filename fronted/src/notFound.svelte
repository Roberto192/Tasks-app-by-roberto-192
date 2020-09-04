<script>
	import {link} from "svelte-routing"
</script>

<div class="container">
	<div class="center">
		<h1>Not Found page</h1>
		<a use:link href="/"> <i class="fas fa-angle-double-left"></i> Back go</a>
	</div>
</div>

<style>

	.container{
		padding: 1rem;
	}

	.center{
		display: flex;
		justify-content: center;
		text-align: center;
	}

	h1{
		color: #4e0a0a;
	}

	a{
		margin-left: 2rem;
		padding: 10px 0;
	}
</style>