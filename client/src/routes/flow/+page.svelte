<script lang="ts">
    import type { PageProps } from './$types';
    let { data } = $props();
</script>
<div class="w-svh py-6 px-4">
    <h1 class="text-2xl font-bold text-gray-800 mb-6">Flows Dashboard</h1>
    <ul class="divide-y divide-gray-200">
        {#each data.fake_data as item (item.id)}
            <li class="p-4 hover:bg-gray-50">
                <a href="/flow/{item.id}" class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
                    <div>
                        <p class="text-xl font-semibold text-gray-900">{item.name}</p>
                        <p class="text-sm text-gray-600">Created on: {item.create_date}</p>
                    </div>
                </a>
            </li>
        {/each}
    </ul>
</div>