import axios from "axios";
export const baseURL = "http://unit-converter-791446476.us-east-1.elb.amazonaws.com:8000/api/";

const getFunc = (path) => {
	return new Promise((resolve, reject) => {
		axios
			.get(`${baseURL}${path}`)
			.then((res) => {
				return resolve({ ...res.data });
			})
			.catch(({ response }) => {
				return reject({ response });
			});
	});
};

const postFunc = (path, payload) => {
	return new Promise((resolve, reject) => {
		axios
			.post(`${baseURL}${path}`, payload)
			.then((res) => {
				return resolve({ ...res });
			})
			.catch(({ response }) => {
				return reject({ response });
			});
	});
};

export { getFunc, postFunc };
