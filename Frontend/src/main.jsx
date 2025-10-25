import React from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'

function Main() {
  return <App />
}

createRoot(document.getElementById('root')).render(<Main />)
