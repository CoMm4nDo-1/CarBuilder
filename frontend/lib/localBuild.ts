const KEY='carbuilder_build'
export const loadBuild=()=>JSON.parse(localStorage.getItem(KEY)||'[]')
export const saveBuild=(v:any)=>localStorage.setItem(KEY,JSON.stringify(v))
