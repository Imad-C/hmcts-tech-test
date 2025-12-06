import type { Task, TaskPayload } from "./types";

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

export async function getTasks(): Promise<Task[]> {
  const resp = await fetch(`${BACKEND_URL}/tasks`);
  const data = await resp.json();

  return data;
}

export async function addTask(payload: TaskPayload): Promise<Task> {
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
