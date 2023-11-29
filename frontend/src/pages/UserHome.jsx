import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import axios from 'axios';

import './UserHome.css'
import SideBar from '../components/SideBar'
import Navbar from '../components/Navbar';
import DetailsBar from '../components/DetailsBar';



const Data = () => {

  const userObjects = useSelector((state) => state.allObjects.userObjects);
  const loggedUser = useSelector((state) => state.userOps.loggedInUserID);

  console.log(userObjects)
  console.log("loggedUser : ", loggedUser)

  return (
    <>
      {
        userObjects.length !== 0 ?

          <div className='d-flex flex-row flex-wrap overflow-x-hidden overflow-y-scroll' style={{ height: '90vh' }}>
            {
              userObjects.map((userObject, index) => {
                return <div key={index}
                  className='card border border-light-subtle rounded overflow-hidden p-2'
                  style={{ margin: '10px 20px 10px 0px', height: "100px", width: "150px" }}
                  onClick={() => { }}>{userObject.title}</div>
              })
            }
          </div>
          : <div className='d-flex flex-row flex-wrap overflow-x-hidden overflow-y-hidden' style={{ height: '90vh' }}>Your Cloud Drive is Hungy!</div>

      }
    </>
  );
}


const UserHome = () => {
  const [selectedPost, setSelectedPost] = useState({})

  return (
    <div className='d-flex flex-row'>
      <SideBar />
      <div className='d-flex flex-column'>
        <Navbar />
        <div className='d-flex flex-row' style={{ margin: '10px 15px' }}>
          <Data />
          <DetailsBar selectedPost={selectedPost} />
        </div>

      </div>

    </div>
  );
}

const mapStateToProps = (state) => {
  return {
    userObjects: state.allObjects.userObjects
  }
}

export default UserHome