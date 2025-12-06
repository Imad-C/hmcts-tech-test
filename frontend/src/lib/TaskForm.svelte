<script lang="ts">
  import type { TaskPayload } from "./types";
  import { addTask } from "./tasks";
  import {
    getTasksError,
    pushTasksStore,
    setTasksError,
  } from "./tasksStore.svelte";

  let taskForm: HTMLFormElement;
  let title: string;
  let description: string;
  let status: string;
  let due: Date;

  async function handleAddTask(event: SubmitEvent) {
    event.preventDefault();

    const payload: TaskPayload = { title, description, status, due };
    try {
      const task = await addTask(payload);
      pushTasksStore(task);
      taskForm.reset();
      setTasksError("");
    } catch (error: any) {
      setTasksError(error.message);
    }
  }
</script>

<div>
  <form bind:this={taskForm} onsubmit={handleAddTask} class="task-form">
    <div class="task-form-input">
      <label for="task-title">Title</label>
      <input
        type="text"
        id="task-title"
        bind:value={title}
        class="input-field"
      />
    </div>
    <div class="task-form-input">
      <label for="task-description">Description</label>
      <textarea
        id="task-description"
        bind:value={description}
        class="description input-field"
      ></textarea>
    </div>
    <div class="task-form-input">
      <label for="task-status">Status</label>
      <select id="task-status" class=" input-field" bind:value={status}>
        <option value="todo">Todo</option>
        <option value="started">Started</option>
        <option value="completed">Complete</option>
      </select>
    </div>
    <div class="task-form-input">
      <label for="task-due">Due</label>
      <input
        type="datetime-local"
        id="task-due"
        bind:value={due}
        class="input-field"
      />
    </div>

    <button type="submit" class="add-task">Add Task</button>
  </form>

  {#if getTasksError()}
    <div class="error-container">
      <p>{getTasksError()}</p>
    </div>
  {/if}
</div>

<style>
  .task-form {
    background: rgb(245, 245, 245);
    position: sticky;
    top: 10px;
    height: fit-content;
    padding: 10px;
    border: solid black 1px;
    margin-bottom: 20px;
    border-radius: 7px;
    box-shadow: 5px 5px 0px black;
  }

  .task-form-input {
    display: flex;
    flex-direction: column;
    margin-bottom: 5px;
  }

  .input-field {
    border: solid black 2px;
    border-radius: 2px;
    padding: 5px;
  }

  .description {
    height: 100px;
  }

  .add-task {
    background: none;
    margin-top: 10px;
    font-size: 1rem;
    display: block;
    margin-left: auto;
    border: solid black 2px;
    padding: 5px;
  }

  .add-task:hover {
    cursor: pointer;
    background: gray;
  }

  .error-container {
    color: red;
    font-weight: bold;
    padding: 5px;
    border: solid red 2px;
    border-radius: 7px;
    box-shadow: 3px 3px 0px lightsalmon;
  }
</style>
