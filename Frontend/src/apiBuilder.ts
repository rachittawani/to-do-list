import axios from "axios";
import Cookies from 'js-cookie';
import type { AxiosRequestConfig, AxiosResponse } from "axios";

export const getRequest = (url: string): Promise<AxiosResponse> => {
	const headers = {
		headers: {BACKEND_ID: BackendID}
    };
	return axios.get(url, headers);
};

export const getRequestWithData = (url: string, data: any): Promise<AxiosResponse> => {
	const headers = {
		BACKEND_ID: BackendID
	};
	const config: AxiosRequestConfig = {
		params: data,
		headers: headers
	};
	return axios.get(url, config);
};

export const postRequest = (url: string, data: any): Promise<AxiosResponse> => {
	return axios.post(url, data);
};

export const postRequestWithId = (url: string, data: any): Promise<AxiosResponse> => {
	const headers = {
        headers:{
            'Content-Type': 'application/x-www-form-urlencoded'
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

export const putRequest = (url: string, data: any): Promise<AxiosResponse> => {
	const headers = {
		headers: {
			BACKEND_ID: BackendID
		}
	};
	return axios.put(url, data, headers);
};

export const putRequestWithData = (url: string, data: any): Promise<AxiosResponse> => {
	const headers = {
		BACKEND_ID: BackendID
	};
	const config: AxiosRequestConfig = {
		params: data,
		headers: headers
	};

	return axios.put(url, data, config);
};

export const deleteRequest = (url: string, data: any): Promise<AxiosResponse> => {
	const headers = {
		BACKEND_ID: BackendID
	};

	const config: AxiosRequestConfig = {
		headers: headers,
		data: data
	};

	return axios.delete(url, config);
};

export const deleteRequestWithData = (url: string, data: any): Promise<AxiosResponse> => {
	const headers = {
		BACKEND_ID: BackendID
	};

	const config: AxiosRequestConfig = {
		headers: headers,
		params: data
	};

	return axios.delete(url, config);
};

export const deleteRequestWithId = (url: string): Promise<AxiosResponse> => {
	const headers = {
		headers: { BACKEND_ID: BackendID }
	};
	return axios.delete(url, headers);
};