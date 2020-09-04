<script>
	import { Router, Route, Link, link } from "svelte-routing"
	import ButtonCustom from "./btn.svelte"

	export let name = "Home"

	export let userName = Globallog

	export let isLogin = false

	const onLogout = async (e)=>{
		e.preventDefault()
		await fetch("/api/logout")
				.then(e => {return e.json()})
				.then(e => {
					if (e.code === 0) {
						location.href = "/"
					}
				})
	}

	const onMenu = (e) => {
		let menu = document.querySelector(".menu")
		menu.classList.toggle("rotate")
		let shows = document.querySelectorAll(".links")
		shows.forEach(e => e.classList.toggle("hide"));
	}
</script>

<div class="header">
	<header>
		<a href="/" use:link class="link"><i class="fas fa-home"></i> {name}</a>
	</header>
	<div on:click = {onMenu} class="menu rotate" id="menu"><i class="fas fa-bars"></i></div>
	<nav class="links hide">
		<Router>
			{#if !isLogin}
				<a use:link on:click={onMenu} href="/register"><i class="fas fa-plus-square"></i> Register</a>
				<a use:link on:click={onMenu} href="/login"><i class="fas fa-sign-in-alt"></i> Login</a>
			{:else}
				<a use:link on:click={onMenu} href="/user"><i class="fas fa-user-circle"></i> {userName}</a>
				<a on:click={onMenu} class="logout" href="/" on:click={onLogout}><i class="fas fa-sign-out-alt"></i> Logout</a>
			{/if}
			<a use:link on:click={onMenu} href="/tasks"><i class="fas fa-thumbtack"></i> My tasks</a>
		</Router>
	</nav>
</div>

<style>
	header{
		width: 100%;
		margin-left: 0.5rem;
		padding: 1rem 0;
		background-color: black;
		z-index: 100;
	}

	a{
		text-decoration: none;
		color: white;
		border: none;
	}

	.header{
		padding: 1rem;
		display: block;
		position: sticky;
		top: 0;
		background: black;
	}

	.link{
		font-size: 2rem;
	}

	.links{
		padding: 1.5rem 0;
	}

	.links a:hover{
		border-bottom: 1px solid white;
	}

	.links a{
		padding: 1rem;
		margin-right: 1rem;
		color: #bbe;
	}

	.menu{
		position: absolute;
		right: 0;
		top: 1.5rem;
		margin: 0 2rem;
		z-index: 3;
		display: none;
	}

	.menu i{
		font-size: 3rem;
		color: white;
		transition: all 1s cubic-bezier(0, 0.02, 0, 1.28) 0.05s;
	}

	.links a.logout{
		cursor: pointer;
	}

	@media screen and (max-width: 500px) {

		.menu{
			cursor: pointer;
			display: block;
			transition: all 1s cubic-bezier(0, 0.02, 0, 1.28) 0.05s;
		}

		.menu:hover i, .menu:focus i{
			text-shadow: 0 0 5px #fff;
		}

		.menu.rotate{
			transform: rotate(1440deg) !important;			
		}

		.links{
			margin: 0;
			position: absolute;
			top: 100%;
			left: 0;
			right: 0;
			background: black;
			z-index: 2;
			transition: all 0.5s ease-in-out 0.25s;
			padding-bottom: 1.5rem;
		}

		.links a{
			display: block;
			width: 100%;			
		}

		.links a:hover{
			border-bottom: 0;
		}

		.hide{
			top: -1000px;
			background: #0000;
		}
	}
	
</style>