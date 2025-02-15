<script>

</script>

<div>
    <div class="flex h-screen">
        <!-- Main content -->
        <div class="flex-1 p-6">
            <h1 class="text-2xl font-bold mb-4">My Projects</h1>
            <div class="fixed bottom-6 right-6">
                <button class="bg-blue-500 hover:bg-blue-600 text-white px-6 py-3 rounded-full shadow-lg flex items-center">
                    <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                    </svg>
                    Add Documents
                </button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {#each Array(3) as _, i}
                    <a href="/documents/{i}" class="block p-4 bg-white rounded-lg shadow hover:shadow-lg transition-shadow">
                        <h2 class="text-lg font-semibold">Project {i + 1}</h2>
                        <p class="text-gray-600">Click to view details</p>
                    </a>
                {/each}
            </div>
        </div>
    </div>

</div>