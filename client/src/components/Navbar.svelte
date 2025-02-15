<script lang="ts">
    import { page } from '$app/stores';
    import { onMount } from 'svelte';

    interface MenuConfig {
        href: string;
        label: string;
    }
    
    export let menuConfig: MenuConfig[] = [
        { href: '/documents', label: 'Home' },
        { href: '/auth', label: 'Sign In' },
        { href: '/stores-ui', label: 'Stores' },
    ];

    export let selected_color = "text-indigo-600";
    
    // Use $page store to track current path
    $: currentPath = $page.url.pathname;
    
    // Helper function to check if a link is active
    function isActive(href: string): boolean {
        // Remove trailing slash for comparison
        const normalizedPath = currentPath.endsWith('/') ? currentPath.slice(0, -1) : currentPath;
        const normalizedHref = href.endsWith('/') ? href.slice(0, -1) : href;
        
        // Exact match for home page
        if (href === '/') {
            return normalizedPath === '';
        }
        
        // For other pages, check if the current path starts with the href
        return normalizedPath === normalizedHref;
    }
</script>

<header class="bg-white shadow-md">
    <nav class="max-w-12xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        <div class="flex items-center">
            <a 
                href="/" 
                class="text-xl font-bold text-indigo-600"
            >
                WOW
            </a>
        </div>
        <div class="flex items-center space-x-4">
            {#each menuConfig as { href, label }}
                <a 
                    {href}
                    class={`px-4 py-2 rounded-md transition-all duration-200 relative
                           ${isActive(href) ? `${selected_color} font-medium` : 'text-gray-600'}
                           hover:text-indigo-600 hover:bg-indigo-50
                           flex items-center space-x-1 group`}
                    aria-current={isActive(href) ? 'page' : undefined}
                >
                    <span>{label}</span>
                </a>
            {/each}
        </div>
    </nav>
</header>