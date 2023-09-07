import { useState } from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom"
import HomePage from "./pages/HomePage"
import Navbar from "./components/Navbar"
import HomeBank from './pages/HomeBank'

function App() {

  return (
    <>
     <BrowserRouter>
      <div className="container mx-auto px-10">
        <Navbar/>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/bank/home" element={<HomeBank />} />
        </Routes>
      </div>
    </BrowserRouter>
    </>
  )
}

export default App
