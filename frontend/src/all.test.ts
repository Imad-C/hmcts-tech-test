import { vi, expect, test } from "vitest";
import { formatDatetime } from "./lib/utils";
import { getTasks, addTask } from "./lib/tasks";

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

const exampleTask = {
  id: 1,
  title: "Test Task",
  description: "Test Task Description",
  status: "todo",
  due: "2025-01-01T12:00:00",
};

const exampleTaskPayload = {
  title: "Test Task",
  description: "Test Task Description",
  status: "todo",
  due: "2025-01-01T12:00:00",
};

test("formatDateTime", () => {
  let dateTime = "2025-12-01T12:30:00";
  expect(formatDatetime(dateTime)).toEqual("01/12/25 12:30");
});

test("getTasks", async () => {
  const tasks = [exampleTask];

  globalThis.fetch = vi.fn().mockResolvedValue({
    ok: true,
    json: () => Promise.resolve(tasks),
  });

  const result = await getTasks();
  expect(result).toEqual(tasks);
  expect(fetch).toHaveBeenCalledWith(`${BACKEND_URL}/tasks`);
});

test("addTask", async () => {
  globalThis.fetch = vi.fn().mockResolvedValue({
    ok: true,
    json: () => Promise.resolve(exampleTask),
  });

  const result = await addTask(exampleTaskPayload);
  expect(result).toEqual(exampleTask);

  expect(fetch).toHaveBeenCalledWith(`${BACKEND_URL}/tasks`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(exampleTaskPayload),
  });
});
