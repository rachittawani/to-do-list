import { TaskState } from "../Task/index";

const taskGetters = {
  newTask(state: TaskState) {
    if(state.newTask == null) {
        state.newTask = JSON.parse(localStorage.getItem('taskObject'))
    }
    return state.newTask;
  }
};

export default taskGetters;