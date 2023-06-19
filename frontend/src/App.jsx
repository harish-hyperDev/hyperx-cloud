import React, { useEffect, useState } from 'react';
import { Routes, Route } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'

// import { Sidebar, Menu, MenuItem, useProSidebar } from "react-pro-sidebar";
import UserHome from './pages/UserHome'
import LandingPage from './pages/LadingPage';
import UserRegistration from './pages/UserRegistration';

function App() {


  // const { collapseSidebar } = useProSidebar();
  return (
    <div style={{ display: 'flex' }}>
      <Routes>
        <Route path='/' element={<LandingPage />} />
        <Route path='/register' element={<UserRegistration />} />
        <Route path='/user' element={<UserHome/>} />
      </Routes>
    </div>
  )
}

export default App
