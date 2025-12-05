import type { Todo, TodoPayload } from "./types";

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

export async function addTask(payload: TodoPayload): Promise<Todo> {
  const resp = await fetch(`${BACKEND_URL}/tasks`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const data = await resp.json();

  return data;
}
