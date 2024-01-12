export interface IProduct {
  title: string;
  pertange_discount: number;
  price: number;
  brand: string;
  is_new: boolean;
  category_id: number;
}

export interface ICategory {
  name: string;
  description: string;
}

export interface IBody {
  product: IProduct;
  category: ICategory;
}
