import React, { useState } from 'react';
import axios from 'axios';

import { CUSTOM_HEADERS } from '../utils/axiosHeaders'
import { USER_OBJECTS_URL } from '../utils/allUrls'

function FileUpload() {
    const [file, setFile] = useState()

    function handleFileChange(event) {
        event.preventDefault()
        setFile(event.target.files[0])
    }

    const handleFileSubmit = async (event) => {
        event.preventDefault()

        const formData = new FormData();
        console.log(file)
        formData.append('file', file);
        formData.append('fileName', file.name);

        const MODIFIED_HEADERS = CUSTOM_HEADERS;
        MODIFIED_HEADERS['headers']['content-type'] = 'multipart/form-data';

        console.log(MODIFIED_HEADERS)
        console.log(formData)
        await axios.post(`${USER_OBJECTS_URL}/upload`, formData, MODIFIED_HEADERS)
        .then((response) => {
            console.log("GOT : ", response.data);
        })

    }

    return (
        <div className="file-upload position-absolute d-flex h-50">
            <form onSubmit={handleFileSubmit}>
                <h1>React File Upload</h1>
                <input type="file" onChange={handleFileChange} />
                <button type="submit">Upload</button>
            </form>
        </div>
    );
}

export default FileUpload