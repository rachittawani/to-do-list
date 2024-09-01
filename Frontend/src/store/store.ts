import { InjectionKey } from "vue";
import { createStore, Store, useStore as baseUseStore } from "vuex";
import taskModule, { TaskState } from "./Task";

export interface State {
  taskMod: TaskState;
}

// eslint-disable-next-line symbol-description
export const storeKey: InjectionKey<Store<State>> = Symbol();

export const store = createStore<State>({
  modules: {
    taskMod: taskModule
  },
});

export function useStore() {
  return baseUseStore(storeKey);
}