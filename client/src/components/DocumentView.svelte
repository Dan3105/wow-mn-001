<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import * as pdfjs from 'pdfjs-dist';
    
    let { url } = $props();

    if (!url) {
        return;
    }

	pdfjs.GlobalWorkerOptions.workerSrc =
		'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.5.141/pdf.worker.min.js';

	export let url = '';
	let canvasContainer: HTMLDivElement;

	async function renderPage(page: pdfjs.PDFPageProxy) {
		const viewport = page.getViewport({ scale: 1.2 });

		const wrapper = document.createElement('div');
		wrapper.style.marginBottom = '16px';
		wrapper.style.position = 'relative';
		wrapper.id = `page-${page._pageIndex + 1}`;
		const canvas = document.createElement('canvas');
		const ctx = canvas.getContext('2d');

		if (!ctx) {
			return;
		}

		canvas.height = viewport.height;
		canvas.width = viewport.width;
		wrapper.appendChild(canvas);
		canvasContainer.appendChild(wrapper);

		page.render({
			canvasContext: ctx,
			viewport: viewport
		});

		const textLayer = document.createElement('div');
		textLayer.className = 'textLayer';
		const textContent = await page.getTextContent();
		pdfjs.renderTextLayer({
			textContentSource: textContent,
			viewport: page.getViewport(),
			container: textLayer
		});

		wrapper.appendChild(textLayer);
	}

	let destroyed = false;
	onMount(async () => {
		const pdfDoc = await pdfjs.getDocument(url).promise;

		if (destroyed) {
			return;
		}

		for (let num = 1; num <= pdfDoc.numPages; num++) {
			pdfDoc.getPage(num).then(renderPage);
		}
	});

	onDestroy(() => {
		destroyed = true;
	});
</script>

<div class="pdf-container">
{#if url}
	<div bind:this={canvasContainer} class="pdf-wrapper" style="--scale-factor: 1.2" />
{#else}
    <div class="bg-gray-100 rounded-lg p-6 text-center h-full">
        <svg class="w-12 h-12 mx-auto text-gray-400 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
        </svg>
        <h3 class="text-lg font-medium text-gray-900">No document selected</h3>
        <p class="mt-2 text-gray-500">Select a document from the list</p>
    </div>
{/if}
</div>

<style>
	.pdf-container {
		height: calc(100vh - 80px);
	}
	.pdf-wrapper {
		flex: 1;
		background: #eee;
		padding: 16px;
		display: flex;
		flex-direction: column;
		align-items: center;
		overflow-y: scroll;
		max-height: 100%;
	}
</style>
