<script>
	const onRegister = async (e)=>{
		e.preventDefault()
		let init = {
			method: "POST",
			body: new FormData(document.getElementById("form-register"))
		}

		await fetch("/api/register", init)
				.then(res => {return res.json()})
				.then(e => {
					if (e.code === 0) {
						location.href = "/login"
					}
				})
				.catch(err => console.log("An error has occurred: ",err))
	}
</script>

<div class="container">
	<form id="form-register" on:submit={onRegister}>
		<h1>Register</h1>
		<hr>
		<div class="group">
			<i class="fas fa-user"></i>
			<input name="username" type="text" placeholder="User name: example Jhon" autofocus required minlength="10">
		</div>
		<div class="group">
			<i class="fas fa-envelope"></i>
			<input name="email" type="email" placeholder="email: example eltojhon99@gmail.com" required>
		</div>
		<div class="group">
			<i class="fas fa-lock"></i>
			<input name="password" type="password" placeholder="password: exmaple mySecretPassword" required minlength="8">
		</div>
		<button>Register</button>
	</form>
</div>

<style>

	form{
		width: 75%;
		margin: auto;
		padding: 2.5rem;
		padding-bottom: 1rem;
		text-align: center;
		border-radius: 0.3rem;
		color: #000;
	}

	input, button{
		border: none;
	}

	input{
		width: 95%;
		background: transparent;
		border-bottom: 2px solid #0005;
		padding: 0.5rem 0 0.75rem 0;
		outline: none;
	}

	input:focus{
		border-bottom: 2px solid #aaa;
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

	h1{
		margin-bottom: 2rem;
	}

	.group{
		margin: 2rem 0;
	}

	@media screen and (max-width: 540px) {
		form{
			width: 100%;
		}	
	}
</style>