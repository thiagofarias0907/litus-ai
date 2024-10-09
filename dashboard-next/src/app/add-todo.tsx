import { revalidateTag } from "next/cache"
import { LoadButton } from "./load-button"

export function AddTodo(){

    async function handleCreateTodo(form:FormData) {
        'use server'


        const title = form.get('title')
        const estimated_time = Number(form.get('estimated-time'))
        
        const toDo = JSON.stringify({title,estimated_time})

        const headers = {"Content-Type": "application/json; charset=utf8"}
        
        if (!title || !estimated_time) {
            return
        }



        await fetch(`${process.env.API_HOST}/todos/insert`, {
            method: 'POST',
            body: toDo,
            headers:headers
        })
        
        revalidateTag('get-todos')
    }

    return (
        <form action={handleCreateTodo}>
            <div className="flex justify-center">
                <div className="flex-wrap space-x-2 mt-10 rounded-md shadow-sm">
                    
                    <div className="flex md:inline-block space-x-1">
                        <label htmlFor="title" className="inline-block text-sm font-medium leading-6 text-gray-900">ToDo</label>
                        <input id="title" name="title" type="text" placeholder="Insert todo description..." 
                            pattern="((?!\s+)(?![\w\d]))|((?!^\s+$).{3,})"
                            required
                            className="peer md:w-60 w-full inline-block rounded-md border-0 py-1.5 pl-2 pr-2 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500"/>
                        <span className="pr-2 hidden text-sm text-red-500 peer-[&:not(:placeholder-shown):not(:focus):invalid]:inline-block">Insert a title with at least 3 characters</span>    
                    </div>
                    
                    <div className="md:inline-block space-x-1">
                        <label htmlFor="estimated-time" className="inline-block text-sm font-medium leading-6 text-gray-900 ">
                            Estimated time (min)
                        </label>
                        <input id="estimated-time" name="estimated-time" placeholder="0" 
                            pattern="\d+"
                            required
                            className="peer inline-block w-10  rounded-md border-0 py-1.5 pl-2 pr-2 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500"/>
                        <span className="pr-2 hidden text-sm text-red-500 peer-[&:not(:placeholder-shown):not(:focus):invalid]:inline-block">Insert a positive integer value</span>    

                    </div>
                    <LoadButton />
                </div>
                <div id='form-validator-message'></div>
            </div>
        </form>
    )
}