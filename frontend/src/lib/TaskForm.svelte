<script lang="ts">
  import type { TodoPayload } from "./types";
  import { addTask } from "./tasks";

  let taskForm: HTMLFormElement;
  let title: string;
  let description: string;
  let status: string;
  let due: Date;

  async function handleAddTask(event: SubmitEvent) {
    event.preventDefault();

    const payload: TodoPayload = { title, description, status, due };
    const task = await addTask(payload);
    console.log(task);

    taskForm.reset();
  }
</script>

<form bind:this={taskForm} onsubmit={handleAddTask} class="task-form">
  <div class="task-form-input">
    <label for="task-title">Name</label>
    <input type="text" id="task-title" bind:value={title} />
  </div>
  <div class="task-form-input">
    <label for="task-description">Description</label>
    <input type="text" id="task-description" bind:value={description} />
  </div>
  <div class="task-form-input">
    <label for="task-status">Status</label>
    <input type="text" id="task-status" bind:value={status} />
  </div>
  <div class="task-form-input">
    <label for="task-due">Due</label>
    <input type="date" id="task-due" bind:value={due} />
  </div>

  <button type="submit" class="add-task">Add</button>
</form>

<style>
  .task-form {
    display: inline-flex;
    flex-direction: column;
    gap: 5px;
    padding: 10px;
    border: solid black 1px;
  }

  .task-form-input {
    display: flex;
    flex-direction: column;
  }

  .add-task {
    margin-top: 5px;
  }
</style>
