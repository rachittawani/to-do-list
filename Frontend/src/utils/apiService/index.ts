import * as APIBuilder from '../../apiBuilder';
import * as CONSTANTS from './urlConstants';

export const getData = () => {
    return APIBuilder.getRequest(CONSTANTS.USER)
}

export const createUser = (data: any) => {
    return APIBuilder.postRequest(CONSTANTS.USER, data);
}

export const login = (data: any) => {
    return APIBuilder.postRequestWithId(CONSTANTS.LOGIN, data);
}

export const getTodo = () => {
    return APIBuilder.getRequestWithAuth(CONSTANTS.TODO)
}