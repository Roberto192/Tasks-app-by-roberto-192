<script>
	export let onBehaviour = ()=>{
			console.log("Click")
		}

	export let name = "Send"

	export let id = ""

</script>

<button on:click={onBehaviour} id="{id}">{name}</button>

<style type="text/css">
	button{
		border-radius: 1rem;
		padding: 1rem;
		color: #fff;
		border: none;
		background: #000a;
	}

	button:hover{
		cursor: pointer;
		background: #000f;
	}

	button:focus{
		outline: none;
		box-shadow: 2px 2px 10px black;
	}
</style>