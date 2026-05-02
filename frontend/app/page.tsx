'use client'
import {useEffect, useMemo, useState} from 'react'
const API=process.env.NEXT_PUBLIC_API_BASE_URL||'http://127.0.0.1:8000'
export default function Page(){
  const [cars,setCars]=useState<any[]>([]); const [carId,setCarId]=useState<number|undefined>()
  const [categories,setCategories]=useState<any[]>([]); const [category,setCategory]=useState('')
  const [parts,setParts]=useState<any[]>([]); const [build,setBuild]=useState<any>({items:[],total_cost:0})
  useEffect(()=>{fetch(API+'/cars').then(r=>r.json()).then((d)=>{setCars(d); if(d[0]) setCarId(d[0].id)})
    fetch(API+'/categories').then(r=>r.json()).then(setCategories)
  },[])
  useEffect(()=>{ if(!carId) return; const q=category?`&category=${encodeURIComponent(category)}`:''; fetch(`${API}/parts?car_id=${carId}${q}`).then(r=>r.json()).then(setParts)},[carId,category])
  const loadBuild=()=>fetch(API+'/build-list').then(r=>r.json()).then(setBuild)
  useEffect(()=>{loadBuild()},[])
  const add=async (part_id:number)=>{await fetch(API+'/build-list/items',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({part_id})});loadBuild()}
  const rm=async (id:number)=>{await fetch(API+'/build-list/items/'+id,{method:'DELETE'});loadBuild()}
  const clear=async ()=>{await fetch(API+'/build-list/clear',{method:'DELETE'});loadBuild()}
  const currentCar=useMemo(()=>cars.find(c=>c.id===carId),[cars,carId])
  return <div className='container'><h1>CarBuilder MVP</h1>
    <div className='card'><strong>Car Selector</strong><div>
      <select value={carId} onChange={e=>setCarId(Number(e.target.value))}>{cars.map(c=><option key={c.id} value={c.id}>{c.make} {c.model} {c.generation} {c.year_start}-{c.year_end} {c.engine}</option>)}</select>
      {currentCar && <span className='muted'> Compatible set: BMW E90 328i (2006–2011) N52</span>}
    </div></div>
    <div style={{margin:'12px 0'}}>
      <button onClick={()=>setCategory('')} style={{marginRight:8}}>All</button>
      {categories.map((c:any)=><button key={c.id} onClick={()=>setCategory(c.name)} style={{marginRight:8, marginTop:8}}>{c.name}</button>)}
    </div>
    <div className='grid'><div className='parts'>{parts.map((p:any)=><div className='card' key={p.id}><h3>{p.name}</h3><div>{p.brand} · {p.category}</div><div><strong>${p.price}</strong></div><div className='muted'>{p.compatibility_notes}</div><div className='muted'>Tags: {p.tags.join(', ')}</div><a href={p.product_url} target='_blank'>View Product</a><div><button onClick={()=>add(p.id)}>Add to Build</button></div></div>)}</div>
      <div className='card sidebar'><h3>Build List</h3>{build.items.map((i:any)=><div key={i.item_id} style={{borderBottom:'1px solid #eee',padding:'8px 0'}}><div>{i.part.name}</div><div>${i.part.price}</div><button onClick={()=>rm(i.item_id)}>Remove</button></div>)}<h4>Total: ${build.total_cost}</h4><button onClick={clear}>Clear Build</button></div></div>
  </div>
}
