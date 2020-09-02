import { postFunc, getFunc } from "./api";

export const createConversion = (payload) => postFunc("convert/", payload);
export const getUnitTypes = () => getFunc("get_units/");
