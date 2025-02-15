<script lang="ts">
    import SidebarFlow from '../../components/SidebarFlow.svelte';
	// Children components
	let { children } = $props();
</script>

<div class="flex min-h-[calc(100vh-4rem)]">
    <SidebarFlow />
    {@render children()}
</div>