import {Car,Category,Part} from './types'
const API=process.env.NEXT_PUBLIC_API_URL||'http://localhost:8000'

async function getJson<T>(url:string, fallback:T):Promise<T>{
  try{
    const res=await fetch(url)
    const data=await res.json()
    return data as T
  }catch{
    return fallback
  }
}

const toArray=<T>(value:unknown):T[] => Array.isArray(value) ? value as T[] : []

export const getCars=async()=>toArray<Car>(await getJson<unknown>(`${API}/cars`,[]))
export const getCategories=async()=>toArray<Category>(await getJson<unknown>(`${API}/categories`,[]))
export const getParts=async(carId:number,category?:string)=>toArray<Part>(await getJson<unknown>(`${API}/parts?car_id=${carId}${category?`&category=${category}`:''}`,[]))
export const getFeatured=async()=>toArray<Part>(await getJson<unknown>(`${API}/parts/featured`,[]))
export const premiumSession=()=>getJson(`${API}/payments/create-premium-session`,{status:'unavailable'})
