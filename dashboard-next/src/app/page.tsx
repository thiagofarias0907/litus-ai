import { Suspense } from "react";
import { AddTodo } from "./add-todo";
import { ToDos } from "./todo";

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-100 to-indigo-100">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="bg-white shadow-lg rounded-xl p-8 min-w-fit">
          <div className="flex justify-center items-center mb-6 ">
            <svg className="w-6 h-6 text-gray-800 mt-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m8.032 12 1.984 1.984 4.96-4.96m4.55 5.272.893-.893a1.984 1.984 0 0 0 0-2.806l-.893-.893a1.984 1.984 0 0 1-.581-1.403V7.04a1.984 1.984 0 0 0-1.984-1.984h-1.262a1.983 1.983 0 0 1-1.403-.581l-.893-.893a1.984 1.984 0 0 0-2.806 0l-.893.893a1.984 1.984 0 0 1-1.403.581H7.04A1.984 1.984 0 0 0 5.055 7.04v1.262c0 .527-.209 1.031-.581 1.403l-.893.893a1.984 1.984 0 0 0 0 2.806l.893.893c.372.372.581.876.581 1.403v1.262a1.984 1.984 0 0 0 1.984 1.984h1.262c.527 0 1.031.209 1.403.581l.893.893a1.984 1.984 0 0 0 2.806 0l.893-.893a1.985 1.985 0 0 1 1.403-.581h1.262a1.984 1.984 0 0 0 1.984-1.984V15.7c0-.527.209-1.031.581-1.403Z"/>
            </svg>
            <h1 className="text-3xl font-bold text-gray-800 pl-3">ToDo</h1>
          </div>
          <div className="rounded-lg p-3">
            <Suspense  fallback="Loading ToDos ...">
              <ToDos/>
            </Suspense>
            <AddTodo/>
          </div>
        </div>
      </div>
    </main>
  );
}
