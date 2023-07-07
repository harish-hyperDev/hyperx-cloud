import SearchBar from "./SearchBar";
import { Button } from 'react-bootstrap';
import FileUpload from "../pages/FileUpload";

import React, { useState } from 'react'

function Navbar() {
  const [uploadModal, setUploadModal] = useState(false);

  return (
    <div className='navbar d-flex flex-row'>
      <SearchBar />
      <Button onClick={() => setUploadModal(true)}>Upload</Button>
      {uploadModal ? <FileUpload /> : null}
    </div>
  )
}

export default Navbar