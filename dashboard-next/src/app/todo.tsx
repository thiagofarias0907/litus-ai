import { DeleteTodo } from "./delete-todo"

export async function ToDos() {
    const response = await fetch(`${process.env.API_HOST}/todos`, {
        next: {
            tags: ['get-todos']
        }
    })
    const data  = await response.json()

    return (
        <ul role="list" className="divide-y divide-gray-100">
            {data.map((todo:ToDo) => (
                <li key={todo._id} className="flex items-center justify-between gap-x-6 p-3 group/item hover:bg-slate-100">
                    <div className="peer flex items-center gap-x-4">
                        <input type="checkbox" className="peer justify-center size-3.5 appearance-none rounded-sm border border-slate-300 accent-indigo-500 dark:accent-indigo-600 checked:appearance-auto"></input>
                        <div className="min-w-0 flex-auto select-none text-slate-700 peer-checked:text-slate-400 peer-checked:line-through">
                            <p className="text-sm font-semibold leading-6 text-gray-900">{todo.title}</p>
                            
                            <div className="flex-wrap justify-between space-x-6 sm:flex-col items-bottom select-none text-xs text-slate-500 peer-checked:text-slate-400 peer-checked:line-through">
                                <p className="inline truncate">Estimated time: {todo.estimated_time} min</p>
                                <p className="hidden sm:inline truncate ">Created at: {todo.creation_time}</p>
                            </div>
                        </div>
                    </div>


                    <DeleteTodo id={todo._id}/>
                
                </li>
            ))}
        </ul>
    )
    
}