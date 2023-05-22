import React, { useState } from 'react'
import './Components.css'

const SearchBar = () => {
  const [searchInput, setSearchInput] = useState("");

  const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value);
  };

  return (
    <div>
      <input
        type="search"
        className='search-bar'
        placeholder="Search here"
        onChange={handleChange}
        value={searchInput} />
    </div>
  );
}

export default SearchBar;

