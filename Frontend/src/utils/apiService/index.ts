import * as APIBuilder from '../../apiBuilder';
import * as CONSTANTS from './urlConstants';

export const getUserDetail = () => {
    return APIBuilder.getRequestWithAuth(CONSTANTS.USER)
}

export const createUser = (data: any) => {
    return APIBuilder.postRequest(CONSTANTS.USER, data);
}

export const login = (data: any) => {
    return APIBuilder.postRequest(CONSTANTS.LOGIN, data);
}

export const getTodo = () => {
    return APIBuilder.getRequestWithAuth(CONSTANTS.TODO)
}

export const createTodo = (data: any) => {
    return APIBuilder.postRequestWithAuth(CONSTANTS.TODO, data)
}

export const changeTodo = (uuid: string, data: any) => {
    return APIBuilder.putRequestWithAuth(CONSTANTS.TODO + "/" + uuid, data)
}

export const deleteTodo = (uuid: string) => {
    return APIBuilder.deleteRequestWithAuth(CONSTANTS.TODO, uuid)
}

export const updatePassword = (data: any) => {
    return APIBuilder.putRequestWithAuth(CONSTANTS.UPDATEPASSWORD, data)
}

export const createLink = (data: any) => {
    return APIBuilder.postRequestWithAuth(CONSTANTS.TAG, data);
}

export const readLink = () => {
    return APIBuilder.getRequestWithAuth(CONSTANTS.TAG)
}

export const deleteLink = (uuid: any) => {
    return APIBuilder.deleteRequestWithAuth(CONSTANTS.TAG, uuid)
}