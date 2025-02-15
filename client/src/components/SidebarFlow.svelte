<script lang="ts">
    import { page } from '$app/stores';

    export let menuConfig = [
        { href: '/documents', label: 'Documents' },
        { href: '/flow', label: 'Flows' },
        { href: '/setting', label: 'Settings' },
    ];

    function handleLogout() {
        // Add logout logic here
        console.log('Logging out...');
    }

    // Track current path
    $: currentPath = $page.url.pathname;

    // Check if link is active
    function isActive(href: string): boolean {
        const normalizedPath = currentPath.endsWith('/') ? currentPath.slice(0, -1) : currentPath;
        const normalizedHref = href.endsWith('/') ? href.slice(0, -1) : href;
        return normalizedPath === normalizedHref;
    }
</script>

<!-- Sidebar -->
<div class="flex min-h-full">
    <div class="w-44 bg-gray-100 p-4 border-l">
        <h2 class="text-xl font-semibold mb-4">Sidebar</h2>
        <ul class="space-y-2">
            {#each menuConfig as { href, label }}
                <li>
                    <a 
                        {href}
                        class="block px-4 py-2 rounded-md transition-all duration-200 relative
                               {isActive(href) ? 'text-indigo-600 font-medium bg-indigo-50' : 'text-gray-600'}
                               hover:text-indigo-600 hover:bg-indigo-50 items-center space-x-1 group"
                        aria-current={isActive(href) ? 'page' : undefined}
                    >
                        <span>{label}</span>
                    </a>
                </li>
            {/each}
            <li>
                <button 
                    type="button"
                    onclick={handleLogout}
                    class="w-full text-left px-4 py-2 rounded-md transition-all duration-200
                           text-red-600 hover:text-indigo-600 hover:bg-indigo-50 items-center space-x-1 group"
                >
                    <span>Logout</span>
                </button>
            </li>
        </ul>
    </div>
</div>