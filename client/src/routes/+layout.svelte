<script lang="ts">
	import '../app.css';
	import Navbar from '../components/Navbar.svelte';
  	import Sidebar from '../components/Sidebar.svelte';

	// Children components
	let { children } = $props();
</script>

<div class="min-h-screen flex flex-col">
	<Navbar />
	<main>
		{@render children()}
	</main>
</div>