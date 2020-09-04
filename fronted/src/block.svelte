<script>
	export let onClose = ()=>{
		document.getElementById("close").outerHTML = ""
	}
	export let name = "Content Block"
</script>

<div on:click|once={onClose} id="close">
	<h2>{name}</h2>
</div>

<style>
	div{
		width: 100%; 
		height: 100%;
		text-align: center;
		position: absolute;
		top: 0;
		left: 0;
		margin: auto;
		color: #fff;
		background: #000e;
	}
	h2{
		text-align: center;
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		margin: auto;
		color: #fff;
	}
</style>