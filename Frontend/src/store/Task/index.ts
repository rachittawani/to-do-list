import taskGetters from "./getters";
import taskMutations from "./mutations";
import { Task } from '../../models/task';

export interface TaskState {
    newTask: Array<Task> | null;
}

const taskModule = {
  namespaced: true,
  state() {
    return {
        newTask: null
    };
  },
  getters: taskGetters,
  mutations: taskMutations,
};

export default taskModule;