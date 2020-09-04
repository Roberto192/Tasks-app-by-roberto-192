<script>

	import Block from "./block.svelte"

	let err = false
	let codeErr = 0

	export let onOptionalFun = ()=>{
		console.log("Your can config this Functions using the prop onOptionalFun")
	}

	const onAuth = async () =>{
		let data = {}
		let init = {
			method: "POST",
			body: new FormData(document.getElementById("form-log"))
		}
		await fetch("/api/login", init)
			.then(res => {return res.json()})
			.then(e => {
				data = e
				if (e.code > 0) {
					err = true
					codeErr = e.code
				}else{
					location.href = "/"
				}
			})
			.catch(err => console.log("An error has occurred: ",err))
			console.log(data)
	}

	const onSubmit = async (e) =>{
		e.preventDefault()
		await onAuth()
		await onOptionalFun()
	}


</script>

<div class="login">
	<form on:submit={onSubmit} class="form" id="form-log">
		<h1>Login</h1>
		<hr>
		{#if err}
			{#if codeErr === 1}
				<span><small>Usuario incorrecto</small></span>
			{:else if codeErr === 2}
				<span><small>Contraseña incorrecta</small></span>
			{:else}
				<span><small>Contraseña o Usuario incorrecto</small></span>
			{/if}
		{/if}
		<div class="form-cont">
			<i class="fas fa-user"></i>
			<input name="username" type="text" placeholder="user name">
		</div>
		<div class="form-cont">
			<i class="fas fa-lock"></i>
			<input name="password" type="password" placeholder="user password">
		</div>
		<div class="form-cont-btn">
			<button>Send</button>
		</div>
	</form>
</div>

<style>

	input, button{
		border: none;
	}

	span{
		color: red !important;
	}

	button{
		width: 100%;
		padding: 1rem;
		background: #0008;
		color: #fff;
	}

	button:hover{
		cursor: pointer;
		background: #000f
	}

	input{
		width: 95%;
		background: transparent;
		border-bottom: 2px solid #0005;
		padding: 0.5rem 0 0.75rem 0;
	}

	input:focus{
		outline: none;
	}

	button:focus{
		outline: none;
		box-shadow: 2px 2px 10px black;
	}

	h1{
		margin-bottom: 2rem;
	}

	.form{
		width: 75%;
		margin: auto;
		padding: 2.5rem;
		padding-bottom: 1rem;
		text-align: center;
		border-radius: 0.3rem;
		color: #000;
	}

	.form-cont{
		margin: 2rem 0;
	}

	.form-cont-btn{
		margin-top: 3rem;
		margin-bottom: 1rem;
	}

	.login{
		display: flex;
		justify-content: center;
	}

	@media screen and (max-width: 540px) {
		.login{
			width: 100%;
			margin: auto;
		}

		.form{
			width: 100%;
		}	
	}
</style>