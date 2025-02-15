<script lang="ts">
    import Tabs from '../../../components/Tabs.svelte';
    import SimpleButton from '../../../components/SimpleButton.svelte';

</script>

<div class="p-6 h-full flex flex-col">
    <a href=".." class="text-blue-500 hover:text-blue-700 mb-4">← Back</a>
    <h1 class="text-2xl font-bold mb-6">Project Details</h1>
    
    <div class="flex bg-white rounded-lg shadow-lg flex-1">  
        <!-- Left column -->
        <div class="w-1/3 flex flex-col p-6 border-r border-gray-200 min-h-0">
            <div class="mb-6 flex-shrink-0">
                <label for="project-title" class="block text-sm font-medium text-gray-700 mb-2">Project Title</label>
                <input 
                    type="text" 
                    class="w-full px-3 py-2 border border-gray-300 rounded-md"
                    placeholder="Enter project title"
                    id="project-title"
                >
            </div>

            <div class="flex items-center justify-between mb-4 flex-shrink-0">
                <h2 class="text-lg font-semibold">Documents</h2>
                <SimpleButton />
            </div>
            
            <div class="overflow-y-auto space-y-3 h-136">
                {#each Array(10) as _, i}
                    <div class="flex items-center justify-between p-3 rounded-md border border-gray-200 hover:bg-gray-50">
                        <div>
                            <span class="font-medium">Document {i + 1}</span>
                            <p class="text-sm text-gray-500">Last modified: Today</p>
                        </div>
                        <button class="px-3 py-1 bg-blue-500 text-white rounded-md hover:bg-blue-600">
                            View
                        </button>
                    </div>
                {/each}
            </div>
        </div>

        <!-- Right column -->
        <div class="w-2/3 p-6">
            <Tabs />
        </div>
    </div>
</div>