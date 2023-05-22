import React from 'react';
import './App.css'

// import { Sidebar, Menu, MenuItem, useProSidebar } from "react-pro-sidebar";
import SideBar from './components/SideBar'
import SearchBar from './components/SearchBar';
import Home from './pages/Home'
// import HomeOutlinedIcon from "@mui/icons-material/HomeOutlined";
// import PeopleOutlinedIcon from "@mui/icons-material/PeopleOutlined";
// import ContactsOutlinedIcon from "@mui/icons-material/ContactsOutlined";
// import ReceiptOutlinedIcon from "@mui/icons-material/ReceiptOutlined";
// import CalendarTodayOutlinedIcon from "@mui/icons-material/CalendarTodayOutlined";
// import HelpOutlineOutlinedIcon from "@mui/icons-material/HelpOutlineOutlined";
// import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";

function App() {

  // const { collapseSidebar } = useProSidebar();
  return (
    <div style={{ display: 'flex' }}>
      <SideBar />
      <div className='app-block'>
        <SearchBar />
        <Home />
      </div>
    </div>
  )
}

export default App
