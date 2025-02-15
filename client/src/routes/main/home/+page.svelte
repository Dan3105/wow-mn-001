<script>

</script>

<div>
    <div class="flex h-screen">
        <!-- Sidebar -->
        <div class="w-64 bg-gray-100 p-4 border-l">
            <h2 class="text-xl font-semibold mb-4">Sidebar</h2>
            <p class="text-gray-600">Future content here</p>
        </div>

        <!-- Main content -->
        <div class="flex-1 p-6">
            <h1 class="text-2xl font-bold mb-4">My Projects</h1>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {#each Array(3) as _, i}
                    <a href="/project/{i}" class="block p-4 bg-white rounded-lg shadow hover:shadow-lg transition-shadow">
                        <h2 class="text-lg font-semibold">Project {i + 1}</h2>
                        <p class="text-gray-600">Click to view details</p>
                    </a>
                {/each}
            </div>
        </div>
    </div>
</div>