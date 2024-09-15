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

export const updatePassword = (data: any) => {
    return APIBuilder.putRequestWithAuth(CONSTANTS.UPDATEPASSWORD, data)
}

export const createLink = (data: any) => {
    return APIBuilder.postRequestWithAuth(CONSTANTS.TAG, data);
}

export const readLink = () => {
    return APIBuilder.getRequestWithAuth(CONSTANTS.TAG)
}

export const deleteLink = (data: any) => {
    return APIBuilder.deleteRequestWithAuth(CONSTANTS.TAG, data)
}