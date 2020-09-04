{#if !isLog}

	<div class="block">
		<div class="conatiner">
			<div class="container" style="text-align: center;">
				<p>Task App it's a SPA (Single Page Application) with Task App you'll be can make tasks to Ordened for priority, you do Register or Login Now!!! </p>
			</div>
			<div class="grid-2">
				<Register></Register>
				<Login></Login>
			</div>
		</div>
	</div>

{/if}

<div class="create hide">
	<form on:submit={onCreateNewTask} id="newTask">
		<div class="close" on:click={onDisplayCreate}><i class="fas fa-times-circle"></i></div>
		<input id="title" type="text" name="title" placeholder="title" autofocus required>
		<textarea id="desc" name="description" placeholder="description" required></textarea>
		<select id="priority" name="priority" required>
			<option value="Select an priority">Select an priority</option>
			<option value="Hight">Hight</option>
			<option value="Medium">Medium</option>
			<option value="Low">Low</option>
		</select>
		<button class="btn-create">
			Create
		</button>
	</form>		
</div>

<h1>My Tasks</h1>
<div class="container container-between">
	<div class="container-block">
		<div class="container-inline" on:click={onDisplayCreate}>
			<i class="fas fa-plus-square"></i>
			<h5 >Add new task</h5>
		</div>
		<hr>
		<button on:click={onDisplayCreate}>Create</button>
	</div>
	<div class="container-block">
		<div class="container-inline">
			<i class="fas fa-tasks"></i>
			<h5>Value</h5>
		</div>
		<hr>
		<select bind:value={value}>
			<option value="none">select a value</option>
			<option value="Hight">Hight</option>
			<option value="Medium">Medium</option>
			<option value="Low">low</option>
		</select>
	</div>
</div>
<hr>
<section class="container">
	{#if tasks}
		<div class="grid">
			{#each tasks as task}
				{#if task.value === value}
					<div class="card card-task">
						<h3>{task.title}</h3>
						<small>{task.value}</small>
						<hr>
						<p>{task.description}</p>
						<hr>
						<div class="container group">
							<button on:click={onEditTasks(task.id)} class="edit">Edit</button>
							<button on:click={onDeleteTasks(task.id)} class="delete">Delete</button>
						</div>
					</div>
				{:else if value == "none"}
					<div class="card card-task">
						<h3>{task.title}</h3>
						<small>{task.value}</small>
						<hr>
						<p>{task.description}</p>
						<hr>
						<div class="container group">
							<button on:click={onEditTasks(task.id)} class="edit">Edit</button>
							<button on:click={onDeleteTasks(task.id)} class="delete">Delete</button>
						</div>
					</div>
				{/if}
			{/each}
		</div>
	{:else}
		<div class="container">
			<h1>Create new task now!!!</h1>
		</div>
	{/if}
</section>

<script>
	import Register from "./Resgister.svelte"
	import Login from "./loginForm.svelte"

	let isLog = Globallog
	let idLog = Globallogid

	let tasks = false
	let idTask = 0

	let value = "none"

	let edit = false

	$: console.log(value)

	const onEditTasks = async (e) => {
		edit = true
		tasks.forEach(task => {
			if (task.id === e){
				idTask = e
				document.querySelector("#title").value = task.title
				document.querySelector("#desc").value = task.description
				document.querySelector("#priority").value = task.value
			}
		});
		onDisplayCreate()
	}

	const onDeleteTasks = async (e) => {
		if (confirm("Do you sure from delete this task?")) {
			let init = {
				method: "DELETE",
			}

			await fetch("/api/deleteTask/"+e, init)
						.then(res => res.json())
						.then(e => {
							console.log(e)
							if(e.code === 0){
								onGetTask()
							}
						})
						.catch(err => console.log(e))
		}
	}

	const onGetTask = async () => {
		await fetch("/api/getTasks/"+idLog)
					.then(res => res.json())
					.then(e => tasks = e.tasks)
					.catch(Err => console.log(Err))
	}

	onGetTask()

	const onDisplayCreate = (e)=>{
		let create = document.querySelector(".create")
		create.classList.toggle("hide")
	}

	const onCreateNewTask = async (e) =>{
		e.preventDefault()
		let newTask = new FormData(document.querySelector("#newTask"))
		if (!edit){
			let init = {
				method: "POST",
				body: newTask
			}

			await fetch("/api/create/"+idLog, init)
						.then(res => res.json())
						.then(e => {
							console.log(e)
							onDisplayCreate()
							onGetTask()
							document.querySelector("#title").value = ""
							document.querySelector("#desc").value = ""
							document.querySelector("#priority").value = ""
						})	
						.catch(err => console.log(''))
		}else{
			let init = {
				method: "PUT",
				body: newTask
			}

			await fetch("/api/edit/"+idTask, init)
						.then(res => res.json())
						.then(e => {
							console.log(e)
							onDisplayCreate()
							onGetTask()
							document.querySelector("#title").value = ""
							document.querySelector("#desc").value = ""
							document.querySelector("#priority").value = ""
							edit = false
						})
						.catch(err => console.log(''))
		}
	}
</script>

<style>

	h1,h2,h3,h4,h5{
		text-align: center;
		margin: 1rem 0;
	}

	hr{
		margin: 0.4rem 0 !important;
	}

	p{
		margin: 2rem;
		padding: 0.5rem;
		overflow: hidden;
		text-overflow: ellipsis;
	}


	button:hover{
		background-color: #000a;
	}

	button, select{
		outline: none;
		border: none;
		padding: 0.9rem;
		width: 100%;
		cursor: pointer;
	}

	select:focus{
		cursor: pointer !important;
	}

	select{
		background-color: #eee;
	}

	form{
		padding: 1rem;
		margin: auto;
		width: 50%;
		background: #168e21a6;
		border-radius: 0.3rem;
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		transition: 1s ease-in-out 0.25s;
	}

	form select{
		background-color: #c6e3c8;
	}

	form input, form button, form textarea{
		border: none;
		margin: 0.5rem 0;
		width: 100%;
		outline: none;
		background: #c6e3c8;
		border-bottom: 1px solid #aaa;
	}

	form input, form textarea{
		padding: 1rem;
	}

	form input:focus, form textarea:focus{
		border-bottom: 2px solid #eee;
	}

	.hide{
		display: none !important;
		width: 0 !important;
		transition: 1s ease-in-out 0.25s;
	}

	.btn-create{
		margin: 1rem 0;
		background: #aaa;
	}

	.btn-create:hover{
		color: white;
		background-color: #000;
	}

	.create{
		position: sticky;
		top: 50%;
		left: 0;
		bottom: 0;
		right: 0;
		display: block;
		transition: 1s ease-in-out 0.25s;
	}

	.close{
		position: absolute;
		top: -26px;
		left: 100%;
		font-size: 2rem;
		color: red;
		cursor: pointer;
	}

	.group{
		margin-bottom: auto !important;
	}

	.group button:nth-child(1){
			margin-right: 0.2rem;
		    border-radius: 0.3rem 0 0 0.3rem;
	}

	.group button:nth-child(1):hover{
		background-color: #00ff;
	}

	.group button:nth-child(2){
			margin-left: 0.2rem;
		    border-radius: 0 0.3rem 0.3rem 0;
	}

	.group button:nth-child(2):hover{
		background-color: #f00f;
	}

	.edit{
		background-color: #1752e4;
	}

	.delete{
		background-color: #f12424;
	}

	.grid{
		width: 100%;
		display: grid !important;
		grid-template-columns: 33% 33% 33% !important;
		gap: 0.5rem !important;
	}

	.grid-2{
		display: grid !important;
		grid-template-columns: 50% 50% !important;
		gap: 0.5rem !important;
	}

	.container{
		display: flex;
		justify-content: center;
		margin: 2rem;
	}

	.container-inline *{
		display: inline-block !important;
	}

	.container-between{
		padding: 1rem;
		display: flex !important;
		justify-content: space-between !important;
	}

	.container-block{
		padding: 0 10rem;
	}

	.container-block *{
		text-align: center;
		display: block;
	}

	.card{
		width: 100%;
		border-radius: 0.3rem;
		padding: 1rem;
		background: #eee;
	}

	.block{
		padding: 2rem;
		position: sticky;
		top: 0;
		left: 0;
		bottom: 0;
		right: 0;
		background-color: #fff;
	}

	@media screen and (max-width: 920px) {
		.grid{
			display: grid !important;
			grid-template-columns: 50% 50% !important;
			gap: 0.5rem !important;
		}

		.grid-2{
			display: grid !important;
			grid-template-columns: 100% !important;
			gap: 0.5rem !important;
		}

		.container-block{
			padding: 0;
		}

		form{
			width: 75%;
		}
	}

	@media screen and (max-width: 500px) {
		.grid{
			display: grid !important;
			grid-template-columns: 100% !important;
			gap: 0.5rem !important;
		}

		.container-between{
			display: block !important;
		}

		.grid-2{
			display: grid !important;
			grid-template-columns: 100% !important;
			gap: 0.5rem !important;
		}

		form{
			width: 80%;
		}
	}
</style>