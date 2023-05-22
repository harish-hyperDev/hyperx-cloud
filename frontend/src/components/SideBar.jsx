import { Sidebar, Menu, MenuItem, SubMenu, useProSidebar } from 'react-pro-sidebar';

import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";
import PersonIcon from '@mui/icons-material/Person';
import PeopleIcon from '@mui/icons-material/People';
import FavoriteIcon from '@mui/icons-material/Favorite';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import SettingsIcon from '@mui/icons-material/Settings';
import LogoutIcon from '@mui/icons-material/Logout';

import '../App.css'
import React, { useState } from 'react';

const SideBar = () => {

  const { collapseSidebar } = useProSidebar();
  const [title, setTitle] = useState("Hyper Cloud")


  return (
    <div className="sidebar" style={{ height: "100vh", display: "flex" }}>
      <Sidebar>
        <Menu style={{ width: 'fit-content', fontFamily: "Neufreit-Bold" }}>
          <MenuItem
            icon={<MenuOutlinedIcon />}
            onClick={() => {
              if (title == "")
                setTitle("Hyper Cloud")
              else
                setTitle("")

              collapseSidebar();
            }}
            style={{ textTransform: 'uppercase' }}
          >
            <h2>{title}</h2>
          </MenuItem>
        </Menu>
        <Menu>
          <MenuItem icon={<PersonIcon />}>My Cloud</MenuItem>
          <MenuItem icon={<PeopleIcon />}>Shared Files</MenuItem>
          <MenuItem icon={<FavoriteIcon />}>Favorites</MenuItem>
          <MenuItem icon={<CloudUploadIcon />}>Upload Files</MenuItem>
        </Menu>
        <Menu>
          <MenuItem icon={<SettingsIcon />}>Settings</MenuItem>
          <MenuItem icon={<LogoutIcon />}>Log Out</MenuItem>
        </Menu>
      </Sidebar>
    </div>
  );
}

export default SideBar;