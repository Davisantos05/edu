import { useEffect, useState } from 'react'
import Card from '../components/ui/Card'
import Button from '../components/ui/Button'
import { apiGet } from '../services/api'

export default function Home({ onBuy }){
  const [courses, setCourses] = useState([])
  const [ebooks, setEbooks] = useState([])

  useEffect(()=>{
    (async()=>{
      try{
        const c = await apiGet('/courses/featured')
        setCourses(c)
      }catch{}
      try{
        const e = await apiGet('/ebooks/popular')
        setEbooks(e)
      }catch{}
    })()
  }, [])

  return (
    <div className="container py-10 space-y-10">
      <section className="text-center space-y-4">
        <h1>EduPlatform</h1>
        <p className="opacity-80">Cursos online e Ebooks — aprenda de forma prática.</p>
      </section>

      <section>
        <div className="flex items-center justify-between mb-3">
          <h2>Cursos em destaque</h2>
          <a className="underline" href="#/dashboard">Dashboard</a>
        </div>
        <div className="grid-cards">
          {courses.map(c => (
            <Card key={c.id}>
              <div className="space-y-2">
                <div className="text-lg font-semibold">{c.title}</div>
                <div className="text-sm opacity-80">{c.instructor}</div>
                <div className="text-sm">R$ {c.price}</div>
                <Button onClick={()=>onBuy({ ...c }, 'course')}>Inscrever-se</Button>
              </div>
            </Card>
          ))}
        </div>
      </section>

      <section>
        <div className="flex items-center justify-between mb-3">
          <h2>Ebooks populares</h2>
        </div>
        <div className="grid-cards">
          {ebooks.map(e => (
            <Card key={e.id}>
              <div className="space-y-2">
                <div className="text-lg font-semibold">{e.title}</div>
                <div className="text-sm opacity-80">{e.author}</div>
                <div className="text-sm">R$ {e.price}</div>
                <Button onClick={()=>onBuy({ ...e }, 'ebook')}>Comprar</Button>
              </div>
            </Card>
          ))}
        </div>
      </section>
    </div>
  )
}
