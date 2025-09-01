import { useEffect, useState } from 'react'
import Card from './ui/Card'
import { apiGet } from '../services/api'

export default function Dashboard(){
  const [stats, setStats] = useState(null)
  const [courses, setCourses] = useState([])
  const [ebooks, setEbooks] = useState([])

  useEffect(()=>{
    (async()=>{
      try{ setStats(await apiGet('/payments/statistics')) } catch{}
      try{ setCourses(await apiGet('/courses')) } catch{}
      try{ setEbooks(await apiGet('/ebooks')) } catch{}
    })()
  }, [])

  return (
    <div className="container py-10 space-y-6">
      <h1>Dashboard</h1>
      <div className="grid md:grid-cols-3 gap-4">
        <Card>
          <div>Total Receita</div>
          <div className="text-2xl font-bold">R$ {stats?.total_revenue?.toFixed?.(2) ?? '0,00'}</div>
        </Card>
        <Card>
          <div>Cursos</div>
          <div className="text-2xl font-bold">{stats?.total_enrollments ?? 0}</div>
        </Card>
        <Card>
          <div>Ebooks</div>
          <div className="text-2xl font-bold">{stats?.total_purchases ?? 0}</div>
        </Card>
      </div>

      <section className="space-y-3">
        <h2>Cursos</h2>
        <div className="grid-cards">
          {courses?.map(c => (
            <Card key={c.id}>
              <div className="font-semibold">{c.title}</div>
              <div className="text-sm opacity-80">{c.instructor}</div>
              <div className="text-sm">R$ {c.price}</div>
            </Card>
          ))}
        </div>
      </section>

      <section className="space-y-3">
        <h2>Ebooks</h2>
        <div className="grid-cards">
          {ebooks?.map(e => (
            <Card key={e.id}>
              <div className="font-semibold">{e.title}</div>
              <div className="text-sm opacity-80">{e.author}</div>
              <div className="text-sm">R$ {e.price}</div>
            </Card>
          ))}
        </div>
      </section>
    </div>
  )
}
