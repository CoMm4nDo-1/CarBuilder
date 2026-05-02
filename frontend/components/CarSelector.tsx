import {Car} from '../lib/types'
export default function CarSelector({cars,carId,onChange}:{cars:Car[];carId:number;onChange:(id:number)=>void}){return <select className='bg-slate-900 p-2 rounded' value={carId} onChange={e=>onChange(Number(e.target.value))}>{cars.map(c=><option key={c.id} value={c.id}>{c.make} {c.model} {c.generation} {c.year_start}-{c.year_end} {c.engine}</option>)}</select>}
