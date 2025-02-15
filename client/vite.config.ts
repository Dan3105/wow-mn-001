import tailwindcss from "@tailwindcss/vite";
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit(), tailwindcss()],
	resolve: {
		alias: {
			$components: '/src/lib/components',
			$stores: '/src/lib/stores',
			$utils: '/src/lib/utils',
		},
	},
});
