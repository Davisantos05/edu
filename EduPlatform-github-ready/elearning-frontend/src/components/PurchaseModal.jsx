import { useState } from 'react'
import Button from './ui/Button'
import { apiPost } from '../services/api'

export default function PurchaseModal({ open, onClose, item, type='course', user }){
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState(null)

  if(!open) return null
  if(!item) return null

  async function handlePay(){
    setLoading(true)
    setMessage(null)
    try {
      const payload = {
        user_id: 1, // demo
        payment_method: 'card',
        amount: item.price,
      }
      if(type==='course'){
        payload.course_id = item.id
        await apiPost('/payments/process-course', payload)
      } else {
        payload.ebook_id = item.id
        await apiPost('/payments/process-ebook', payload)
      }
      setMessage('Compra concluída com sucesso!')
    } catch(e){
      setMessage('Erro: ' + e.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="fixed inset-0 bg-black/60 grid place-items-center z-50">
      <div className="card w-full max-w-md">
        <h2 className="mb-4">Finalizar compra</h2>
        <p className="mb-2"><b>Item:</b> {item.title}</p>
        <p className="mb-4"><b>Preço:</b> R$ {item.price}</p>
        {message && <div className="mb-3 text-sm">{message}</div>}
        <div className="flex gap-2">
          <Button onClick={handlePay} disabled={loading}>{loading ? 'Processando...' : 'Pagar'}</Button>
          <button className="btn-outline" onClick={onClose}>Fechar</button>
        </div>
      </div>
    </div>
  )
}
