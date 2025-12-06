import type { Task } from "./types";
import { getTasks } from "./tasks";

let tasksStore = $state<Task[]>(await getTasks());

export function setTasksStore(tasks: any) {
  tasksStore = tasks;
}

export function getTasksStore() {
  return tasksStore;
}

export function pushTasksStore(task: any) {
  tasksStore.push(task);
}
