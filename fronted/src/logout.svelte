<script>
	const onLogout = async ()=>{
		await fetch("/logout")
				   .then(res => {return res.json()})
				   .then(e => console.log(e))
				   .catch(e => console.log("error: "+e))
	}
</script>

<button on:click={onLogout}>logout</button>

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