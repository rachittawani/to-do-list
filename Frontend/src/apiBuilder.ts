import axios from "axios";
import Cookies from 'js-cookie';
import type { AxiosRequestConfig, AxiosResponse } from "axios";

export const getRequestWithAuth = (url: string): Promise<AxiosResponse> => {
	const token = Cookies.get('token')
    const tokenType = Cookies.get('tokenType')
	const headers = {
        headers:{
            'Authorization': tokenType + ' ' + token
        }
    }
	return axios.get(url, headers);
};

export const postRequest = (url: string, data: any): Promise<AxiosResponse> => {
	const headers = {
        headers:{
            'Content-Type': 'application/json'
        }
    }
	return axios.post(url, data, headers);
};

export const postRequestWithAuth = (url: string, data: any): Promise<AxiosResponse> => {
	const token = Cookies.get('token')
    const tokenType = Cookies.get('tokenType')
	const headers = {
        headers:{
            'Authorization': tokenType + ' ' + token
        }
    }
	return axios.post(url, data, headers);
};

export const putRequestWithAuth = (url: string, data: any): Promise<AxiosResponse> => {
	const token = Cookies.get('token')
    const tokenType = Cookies.get('tokenType')
	const headers = {
        headers:{
            'Authorization': tokenType + ' ' + token
        }
    }
	return axios.put(url, data, headers);
};

export const deleteRequestWithAuth = (url: string, data: any): Promise<AxiosResponse> => {
	const token = Cookies.get('token')
    const tokenType = Cookies.get('tokenType')
	const headers = {
        'Authorization': tokenType + ' ' + token
    }

	const config: AxiosRequestConfig = {
		headers: headers,
		data: data
	};

	return axios.delete(url + '/' + data, config);
};
