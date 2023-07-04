import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import axios from 'axios';

import './UserHome.css'
import SideBar from '../components/SideBar'
import SearchBar from '../components/SearchBar';
import DetailsBar from '../components/DetailsBar';



const Data = ({ setSelectedPost }) => {

  const posts = useSelector((state) => state.allObjects.objects);
  const loggedUser = useSelector((state) => state.userOps.loggedInUserID);

  console.log(posts)
  console.log("loggedUser : ", loggedUser)

  return (
    <div className='d-flex flex-row flex-wrap overflow-x-hidden overflow-y-scroll' style={{ height: '90vh' }}>
      {posts.map((post, index) => {
        return <div key={index}
          className='card border border-light-subtle rounded overflow-hidden p-2'
          style={{ margin: '10px 20px 10px 0px', height: "100px", width: "150px" }}
          onClick={() => { setSelectedPost(post) }}>{post.title}</div>
      })}
    </div>
  )
}


const UserHome = () => {
  const [selectedPost, setSelectedPost] = useState({})

  return (
    <>
      <SideBar />
      <div style={{ margin: '10px 15px' }}>
        <SearchBar />
          <Data setSelectedPost={setSelectedPost} />
      </div>
      <DetailsBar selectedPost={selectedPost} />

    </>
  );
}


export default UserHome