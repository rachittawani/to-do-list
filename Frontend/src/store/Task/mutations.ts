const taskMutations = {
  taskUpdatedStateMgt(state, payload) {
    if(state.newTask!=null || state.newTask!=undefined) {
        let itemIndex;
        for(let i=0;i<state.newTask.length;i++)
        {
            if(state.newTask[i].id == payload.id)
            {
                itemIndex = i;
                break;
            }
            else{
                itemIndex = undefined;
            }
        }
        if(itemIndex != undefined) {
            state.newTask.splice(itemIndex,1)
            state.newTask.push(payload)
        }
        else {
            state.newTask.push(payload)
        }
        localStorage.setItem('taskObject', JSON.stringify(state.newTask));

    }
    else {
        const arr = []
        arr.push(payload)
        state.newTask=arr
        localStorage.setItem('taskObject', JSON.stringify(state.newTask));
    }
    // state.newTask = payload;
  }
};

export default taskMutations;