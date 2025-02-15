import type { PageLoad } from "./$types";

const fake_data = [{ id: 1, name: 'Flow 1', create_date: '2021-01-01'},
    { id: 2, name: 'Flow 2', create_date: '2021-01-02'}
]

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export const load: PageLoad = async ({ params }) => {
    return {
       fake_data: fake_data 
    }
}