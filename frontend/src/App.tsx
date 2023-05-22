import './App.css'

import { Sidebar, Menu, MenuItem, useProSidebar } from "react-pro-sidebar";
// import HomeOutlinedIcon from "@mui/icons-material/HomeOutlined";
// import PeopleOutlinedIcon from "@mui/icons-material/PeopleOutlined";
// import ContactsOutlinedIcon from "@mui/icons-material/ContactsOutlined";
// import ReceiptOutlinedIcon from "@mui/icons-material/ReceiptOutlined";
// import CalendarTodayOutlinedIcon from "@mui/icons-material/CalendarTodayOutlined";
// import HelpOutlineOutlinedIcon from "@mui/icons-material/HelpOutlineOutlined";
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";

function App() {

  const { collapseSidebar } = useProSidebar();
  return (
    <>
      <div id="app" style={({ height: "100vh", display: "flex" })}>
        <Sidebar style={{ height: "100vh" }}>
            <Menu>
              <MenuItem
                icon={<MenuOutlinedIcon />}
                onClick={() => {
                  collapseSidebar();
                }}
                style={{ textAlign: "center" }}
              >
                {" "}
                <h2>Hyper Cloud</h2>
              </MenuItem>
            </Menu>
          </Sidebar>
      </div>
    </>
  )
}

export default App
