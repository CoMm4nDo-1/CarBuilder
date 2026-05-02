'use client'
import {useEffect,useState} from 'react'
import Header from '../components/Header'; import CarSelector from '../components/CarSelector'; import CategoryFilter from '../components/CategoryFilter'; import PartCard from '../components/PartCard'; import BuildList from '../components/BuildList'
import {getCars,getCategories,getParts,getFeatured} from '../lib/api'; import {loadBuild,saveBuild} from '../lib/localBuild'; import {Part} from '../lib/types'
export default function Home(){const [cars,setCars]=useState<any[]>([]);const [carId,setCarId]=useState(0);const [categories,setCategories]=useState<any[]>([]);const [category,setCategory]=useState('');const [parts,setParts]=useState<Part[]>([]);const [featured,setFeatured]=useState<Part[]>([]);const [build,setBuild]=useState<Part[]>([])
useEffect(()=>{getCars().then(c=>{setCars(c);if(c[0])setCarId(c[0].id)});getCategories().then(setCategories);getFeatured().then(setFeatured);setBuild(loadBuild())},[])
useEffect(()=>{if(carId)getParts(carId,category||undefined).then(setParts)},[carId,category])
const add=(p:Part)=>{if(build.some(b=>b.id===p.id)) return; const n=[...build,p]; setBuild(n); saveBuild(n)}
const remove=(id:number)=>{const n=build.filter(b=>b.id!==id);setBuild(n);saveBuild(n)}
const clear=()=>{setBuild([]);saveBuild([])}
return <div><Header/><main className='max-w-7xl mx-auto p-4'><section className='mb-4'><h2 className='text-3xl font-bold'>Plan your BMW E90 328i build</h2><p className='text-slate-400'>PCPartPicker-style workflow for mods, fitment, and pricing.</p></section><div className='mb-3'><CarSelector cars={cars} carId={carId} onChange={setCarId}/></div><CategoryFilter categories={categories} active={category} onPick={setCategory}/><h3 className='mt-6 mb-2 font-semibold'>Featured Parts</h3><div className='grid md:grid-cols-3 gap-3'>{featured.slice(0,3).map(p=><PartCard key={p.id} part={p} onAdd={add}/>)}</div><div className='grid md:grid-cols-[1fr_340px] gap-4 mt-6'><div className='grid md:grid-cols-2 gap-3'>{parts.map(p=><PartCard key={p.id} part={p} onAdd={add}/>)}</div><BuildList items={build} onRemove={remove} onClear={clear}/></div></main></div>}
