import React, { useEffect } from 'react';
import './Components.css'

function DetailsBar( {selectedPost} ) {

  useEffect(() => {
    console.log("detail : ", selectedPost)
    console.log("detail is null? ", Object.is(selectedPost, null))
  },[])
  return (
    <div className="details-bar">
      { 
        Object.is(selectedPost, null) ? <img className='details-thumbnail' src='https://via.placeholder.com/600/f66b97'></img>
                                      : <div className='no-thumbnail'>Select an item to see the details</div>
      }
    </div>
  );
}

export default DetailsBar;