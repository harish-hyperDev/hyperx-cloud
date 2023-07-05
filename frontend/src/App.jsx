import React, { useEffect, useState } from 'react';
import { Routes, Route } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'

// import { Sidebar, Menu, MenuItem, useProSidebar } from "react-pro-sidebar";
import UserHome from './pages/UserHome'
import UserLogin from './pages/UserLogin';
import UserRegistration from './pages/UserRegistration';

function App() {

  // {process.env.NODE_ENV === 'development' ? process.env.REACT_APP_DEV_MODE : process.env.REACT_APP_PRO_MODE}

  // const { collapseSidebar } = useProSidebar();
  return (
    <div style={{ display: 'flex' }}>
      <Routes>
        <Route path='/' element={<UserLogin />} />
        <Route path='/register' element={<UserRegistration />} />
        <Route path='/user' element={<UserHome/>} />
      </Routes>
    </div>
  )
}

export default App
