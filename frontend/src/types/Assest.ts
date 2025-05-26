export type AssetCategory = 'stock' | 'cash' | 'crypto' | 'real_estate' | 'other'


export interface Asset {
    id: string
    name: string
    catrgory: AssetCategory
    amount: number
    currency: string
    date: string
}
