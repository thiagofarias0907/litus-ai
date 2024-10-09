'use client'

import { useFormStatus } from "react-dom";

export function LoadButton(){

    const {pending} = useFormStatus()

    return (
        <button type="submit" disabled={pending} className="inline-block w-30 rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 ">
            {pending ? 'Saving ...' : 'Add new ToDo'}
        </button>
    )
}