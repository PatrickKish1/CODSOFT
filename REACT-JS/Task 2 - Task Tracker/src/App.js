import React, { useState } from 'react';
import TaskList from './components/TaskList';
import AddTaskForm from './components/AddTaskForm';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([]);

  const addTask = (task) => {
    setTasks([...tasks, task]);
  };

  const updateTask = (updatedTask) => {
    setTasks(tasks.map(task => task.id === updatedTask.id ? updatedTask : task));
  };

  const deleteTask = (taskId) => {
    setTasks(tasks.filter(task => task.id !== taskId));
  };

  return (
    <div className="App">
      <header>
        <h1>Task Tracker</h1>
      </header>
      <AddTaskForm addTask={addTask} />
      <div className="task-list-container">
        <h2>CREATED TASKS</h2>
        {tasks.length === 0 ? (
          <p className="no-tasks-message">No task created.</p>
        ) : (
          <TaskList tasks={tasks} updateTask={updateTask} deleteTask={deleteTask} />
        )}
      </div>
    </div>
  );
}

export default App;
