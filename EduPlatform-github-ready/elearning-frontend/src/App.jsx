import { useEffect, useState } from 'react'
import { Routes, Route, Link, useLocation } from 'react-router-dom'
import Home from './pages/Home'
import Dashboard from './components/Dashboard'
import AuthModal from './components/AuthModal'
import PurchaseModal from './components/PurchaseModal'

export default function App(){
  const [authOpen, setAuthOpen] = useState(false)
  const [purchaseOpen, setPurchaseOpen] = useState(false)
  const [purchaseItem, setPurchaseItem] = useState(null)
  const [purchaseType, setPurchaseType] = useState('course')
  const [user, setUser] = useState(null)
  const loc = useLocation()

  useEffect(()=>{
    const u = localStorage.getItem('edu_user')
    if(u) setUser(JSON.parse(u))
  },[])

  function openBuy(item, type){
    if(!user){ setAuthOpen(true); return }
    setPurchaseType(type)
    setPurchaseItem(item)
    setPurchaseOpen(true)
  }

  return (
    <div>
      <header className="border-b border-slate-800">
        <div className="container flex items-center gap-4 py-4">
          <Link to="/" className="font-bold text-lg">EduPlatform</Link>
          <nav className="flex gap-4">
            <Link to="/">Início</Link>
            <Link to="/dashboard">Dashboard</Link>
          </nav>
          <div className="ml-auto flex items-center gap-2">
            {user ? (
              <>
                <span className="text-sm opacity-80">Olá, {user.username}</span>
                <button className="btn-outline" onClick={()=>{localStorage.removeItem('edu_user'); setUser(null)}}>Sair</button>
              </>
            ) : (
              <button className="btn" onClick={()=>setAuthOpen(true)}>Entrar</button>
            )}
          </div>
        </div>
      </header>

      <Routes>
        <Route path="/" element={<Home onBuy={openBuy} />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>

      <AuthModal open={authOpen} onClose={()=>setAuthOpen(false)} onAuth={setUser} />
      <PurchaseModal open={purchaseOpen} onClose={()=>setPurchaseOpen(false)} item={purchaseItem} type={purchaseType} user={user} />
    </div>
  )
}
