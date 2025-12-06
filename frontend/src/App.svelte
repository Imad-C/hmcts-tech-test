<script lang="ts">
  import TaskForm from "./lib/TaskForm.svelte";
  import Tasks from "./lib/Tasks.svelte";
</script>

<main class="layout">
  <TaskForm />
  <Tasks />
</main>

<style>
  .layout {
    width: 50%;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 10px;
  }
</style>
