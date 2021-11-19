import storage from "./StorageService";
import isObjectEmpty from "../helpers/isObjectEmpty";


// const API_BASE_URL = "http://localhost:3000";
const API_BASE_URL = "https://muusikat-api-v1.herokuapp.com";

const constructUrl = (...args) => {
  return API_BASE_URL.concat(args.join("/"));
};

const constructQueryParams = (data) => {
    return !isObjectEmpty(data)
        ?
            "?".concat(Object.keys(data).map(key => `${key}=${data[key]}`).join("&"))
        :
            ""
};

const constructHeaders = (contentType, isAuthRequired) => {
    if (isAuthRequired) {
        return {
            "Content-Type": contentType,
        }
    } else {
        return {
            "Content-Type": contentType,
            "X-Auth-Token": storage.get("MUUSIKAT-TOKEN"),
        }
    }
};

const constructBody = (data, contentType) => {
    return contentType === "application/json;charset=utf-8"
        ? JSON.stringify(data)
        : data;
};

export const sendGET = (url, params = {}) => {
    return fetch(constructUrl(url).concat(constructQueryParams(params)));
};

export const sendPOST = (url, data = [], params = {}, isAuthRequired, contentType = "application/json;charset=utf-8") => {
    return fetch(
        constructUrl(url).concat(constructQueryParams(params)),
        {
            method: "POST",
            headers: constructHeaders(contentType, isAuthRequired),
            body: constructBody(data, contentType)
        }
    )
};

export const sendPUT = (url, data, contentType = "application/json;charset=utf-8" ) => {
    return fetch(
        constructUrl(url),
        {
            method: "PUT",
            headers: constructHeaders(contentType),
            body: constructBody(data, contentType)
        }
    )
};

export const sendDELETE = (url, contentType = "application/json;charset=utf-8") => {
    return fetch(
        constructUrl(url),
        {
            method: "DELETE",
            headers: constructHeaders(contentType)
        }
    )
};
