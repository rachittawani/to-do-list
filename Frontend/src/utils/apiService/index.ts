import * as APIBuilder from '../../apiBuilder';
import * as CONSTANTS from './urlConstants';

export const getData = () => {
    return APIBuilder.getRequest(CONSTANTS.USER)
}

export const createUser = (data: any) => {
    return APIBuilder.postRequest(CONSTANTS.USER, data);
}