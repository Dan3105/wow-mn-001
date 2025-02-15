<script>
    import { writable } from 'svelte/store';
    import { SvelteFlow, Background, Controls } from '@xyflow/svelte';
    import '@xyflow/svelte/dist/style.css';
 
    const nodes = writable([{
        id: '1',
        position: { x: 100, y: 100 },
        data: { label: 'Node 1' }
    }, {
        id: '2',
        position: { x: 300, y: 100 },
        data: { label: 'Node 2' }
    }]);
    const edges = writable([{
        id: '1-2',
        source: '1',
        target: '2'
    }]);
</script>

<main class="w-full h-inherit">
    <SvelteFlow {nodes} {edges}>
        <Background />
        <Controls />
    </SvelteFlow>
</main>