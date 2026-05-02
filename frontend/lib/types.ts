export type Car={id:number;make:string;model:string;generation:string;year_start:number;year_end:number;engine:string}
export type Category={id:number;name:string;slug:string}
export type Part={id:number;name:string;brand:string;current_price:number;product_url:string;affiliate_url?:string;compatibility_notes?:string;tags:string[];is_featured:boolean;is_sponsored:boolean;sponsor_label?:string;vendor_id?:number;image_url?:string}
