const API = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

export async function apiGet(path) {
  const res = await fetch(`${API}${path}`);
  if (!res.ok) throw new Error('Erro ao buscar: ' + path);
  return res.json();
}

export async function apiPost(path, data) {
  const res = await fetch(`${API}${path}`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  });
  const json = await res.json().catch(()=>({}));
  if (!res.ok) throw new Error(json.error || json.message || 'Erro ao enviar');
  return json;
}

export default { apiGet, apiPost };
