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

let tasksError = $state<string>("");

export function setTasksError(error: string) {
  tasksError = error;
}

export function getTasksError() {
  return tasksError;
}

let tasksSuccess = $state<string>("");

export function setTasksSuccess(success: string) {
  tasksSuccess = success;
}

export function getTasksSuccess() {
  return tasksSuccess;
}
