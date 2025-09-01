import { useState } from 'react'

export default function AuthModal({ open, onClose, onAuth }){
  const [isLogin, setIsLogin] = useState(true)
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')

  if(!open) return null

  function handleSubmit(e){
    e.preventDefault()
    const user = isLogin ? { username } : { username, email }
    localStorage.setItem('edu_user', JSON.stringify(user))
    onAuth?.(user)
    onClose?.()
  }

  return (
    <div className="fixed inset-0 bg-black/60 grid place-items-center z-50">
      <div className="card w-full max-w-md">
        <h2 className="mb-4">{isLogin ? 'Entrar' : 'Criar conta'}</h2>
        <form onSubmit={handleSubmit} className="space-y-3">
          <div>
            <label>Usuário</label>
            <input className="input" value={username} onChange={e=>setUsername(e.target.value)} required/>
          </div>
          {!isLogin && (
            <div>
              <label>E-mail</label>
              <input className="input" type="email" value={email} onChange={e=>setEmail(e.target.value)} required/>
            </div>
          )}
          <div className="flex gap-2">
            <button type="submit" className="btn">{isLogin ? 'Entrar' : 'Registrar'}</button>
            <button type="button" className="btn-outline" onClick={onClose}>Cancelar</button>
            <button type="button" className="ml-auto underline" onClick={()=>setIsLogin(v=>!v)}>
              {isLogin ? 'Criar conta' : 'Já tenho conta'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}
