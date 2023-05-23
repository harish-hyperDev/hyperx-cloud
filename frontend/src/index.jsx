import React from 'react'
import ReactDOM from 'react-dom/client'
import { Provider } from 'react-redux'
import App from './App'
import { ProSidebarProvider } from "react-pro-sidebar";
import store from './redux/store'
import './index.css'


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Provider store={store}>
      <ProSidebarProvider>
        <App />
      </ProSidebarProvider>
    </Provider>
  </React.StrictMode>,
);
