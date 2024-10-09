'use client'

const handleDelete = async (id: String) => {
    
    const response = await fetch(`http://localhost:8080/todos/delete/${id}`, {
        method: 'DELETE'
    })
    
    if (response.status != 204){
        alert("Delete operation has failed")
    }
        
}

export function DeleteButton({ id }){

    return (
        
        <button onClick={() => handleDelete(id)} className="shrink-0 size-[26px] rounded-md p-1 text-red-900 hover:bg-red-50 hover:text-red-500 block peer-has-[:checked]:hidden">
            <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
        </button>
    )
}