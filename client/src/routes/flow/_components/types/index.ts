import type { Writable } from "svelte/store";

export interface NodeBase {
    id: string;
    name: string;
    NodeType: string;
    output: unknown;
}

export interface Flow {
    id: Writable<string>;
    nodes: Writable<NodeBase[]>;
}