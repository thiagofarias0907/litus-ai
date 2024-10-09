import { revalidateTag } from "next/cache"

export function DeleteTodo({id}){

    async function handleDeleteTodo(input) {
        'use server'
       
        const response = await fetch(`${process.env.API_HOST}/todos/delete/${input.get('id-value')}`, {
            method: 'DELETE'
        })
        
        if (response.status != 204){
            console.error("Delete operation has failed")
            return
        }
            
        revalidateTag('get-todos')
    }

    return (
        <form action={handleDeleteTodo} className=" peer-has-[:checked]:hidden">
            <input type="hidden" name={"id-value"} value={id}></input>
            <button id={"delete-"+ id} className="shrink-0 size-[26px] rounded-md p-1 text-red-900 hover:bg-red-50 hover:text-red-500 block">
                <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
            </button>
        </form>
    )
}