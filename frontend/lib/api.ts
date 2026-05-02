import {Car,Category,Part} from './types'
const API=process.env.NEXT_PUBLIC_API_URL||'http://localhost:8000'
export const getCars=()=>fetch(`${API}/cars`).then(r=>r.json()) as Promise<Car[]>
export const getCategories=()=>fetch(`${API}/categories`).then(r=>r.json()) as Promise<Category[]>
export const getParts=(carId:number,category?:string)=>fetch(`${API}/parts?car_id=${carId}${category?`&category=${category}`:''}`).then(r=>r.json()) as Promise<Part[]>
export const getFeatured=()=>fetch(`${API}/parts/featured`).then(r=>r.json()) as Promise<Part[]>
export const premiumSession=()=>fetch(`${API}/payments/create-premium-session`,{method:'POST'}).then(r=>r.json())
