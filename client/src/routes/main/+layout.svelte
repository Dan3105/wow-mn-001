<script lang="ts">
  	import Sidebar from '../../components/Sidebar.svelte';

	// Children components
	let { children } = $props();
</script>

<div class="min-h-screen flex flex-col">
	<div class="flex min-h-[calc(100vh-4rem)]">
        <Sidebar/>
		<main class="flex-1 max-w-12xl w-full mx-auto px-4 sm:px-6 lg:px-8">
			{@render children()}
		</main>
	</div>
</div>