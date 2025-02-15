<script>
    export let tabs = [
        { id: 'tab1', label: 'Profile' },
        { id: 'tab2', label: 'Settings' },
    ];
    export let activeTab = 'tab1';
</script>

<div class="tab-container">
    {#each tabs as tab, index}
        <input
            type="radio"
            name="tab"
            id={tab.id}
            class="tab"
            checked={activeTab === tab.id}
            on:change={() => activeTab = tab.id}
        />
        <label class="tab_label" for={tab.id}>{tab.label}</label>
    {/each}
    
    <div class="indicator" style="left: calc({tabs.findIndex(t => t.id === activeTab)} * 130px + 2px)"></div>
</div>

<style>
    .tab-container {
        position: relative;
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        padding: 2px;
        background-color: #dadadb;
        border-radius: 9px;
    }

    .indicator {
        content: "";
        width: 130px;
        height: 34px;
        background: #ffffff;
        position: absolute;
        top: 2px;
        z-index: 9;
        border: 0.5px solid rgba(0, 0, 0, 0.04);
        box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.12), 0px 3px 1px rgba(0, 0, 0, 0.04);
        border-radius: 7px;
        transition: all 0.2s ease-out;
    }

    .tab {
        width: 130px;
        height: 34px;
        position: absolute;
        z-index: 99;
        outline: none;
        opacity: 0;
    }

    .tab_label {
        width: 130px;
        height: 34px;
        position: relative;
        z-index: 999;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 0;
        font-size: 1rem;
        opacity: 0.6;
        cursor: pointer;
    }

    .tab_label:has(+ input:checked) {
        opacity: 1;
    }
</style>
