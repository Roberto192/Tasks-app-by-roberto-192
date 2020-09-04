<script>
	import { Router, Route, Link } from "svelte-routing"
	import Navbar from "./navbar.svelte"
	import Home from "./Home.svelte"
	import Login from "./loginForm.svelte"
	import NotFound from "./notFound.svelte"
	import MyTasks from "./MyTasks.svelte"
	import Register from "./Resgister.svelte"

	const login = Globallog

	console.log("login: "+login)
</script>

<div class="app">
	<Navbar isLogin={login}></Navbar>
	<Router>
		<Route path="/register" component={Register} />
		<Route path="/" component={Home}/>
		<Route path="/home" component={Home}/>
		<Route path="/login" component={Login}/>
		<Route path="/tasks" component={MyTasks} />
		<Route path="*" component={NotFound}/>
	</Router>
</div>

<style>
	.app{
		width: 100%;
		height: 100%;
	}
</style>