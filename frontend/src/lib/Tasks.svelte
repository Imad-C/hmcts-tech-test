<script>
  import { getTasksStore } from "./tasksStore.svelte";
  import { formatDatetime } from "./utils";
</script>

<div class="task-container">
  {#each getTasksStore() as task (task.id)}
    <div class="task-card">
      <p class="task-title">{task.title}</p>
      <div class="task-details">
        <div class="task-meta">
          <p>{task.status}</p>
          <p>{formatDatetime(task.due)}</p>
        </div>
        <p class:task-description={task.description}>{task.description}</p>
      </div>
    </div>
  {/each}
</div>

<style>
  .task-container {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }

  .task-card {
    max-width: 400px;
    padding: 5px;
    border: solid black 1px;
    border-radius: 7px;
    background: rgb(245, 245, 245);
    box-shadow: 3px 3px 0px gray;
  }

  .task-title {
    text-align: center;
    font-weight: 900;
  }

  .task-details {
    background: lightgray;
    border: solid gray 2px;
    border-radius: 4px;
  }

  .task-meta {
    padding: 0px 3px;
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid black;
  }

  .task-description {
    padding: 4px;
  }
</style>
