import React, { useState } from 'react';
import './AddTaskForm.css';

function AddTaskForm({ addTask }) {
  const [task, setTask] = useState({ name: '', date: '', time: '', completed: false });

  const handleSubmit = (e) => {
    e.preventDefault();
    const taskDateTime = new Date(`${task.date}T${task.time}`);
    addTask({ ...task, id: Date.now(), date: taskDateTime });
    setTask({ name: '', date: '', time: '', completed: false });
  };

  return (
    <div className="add-task-form">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Task Name"
          value={task.name}
          onChange={(e) => setTask({ ...task, name: e.target.value })}
          required
        />
        <input
          type="date"
          value={task.date}
          onChange={(e) => setTask({ ...task, date: e.target.value })}
          required
        />
        <input
          type="time"
          value={task.time}
          onChange={(e) => setTask({ ...task, time: e.target.value })}
          required
        />
        <button type="submit" className="create-task-btn">Create Task</button>
      </form>
    </div>
  );
}

export default AddTaskForm;
