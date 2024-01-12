// import { response } from "../../util/utils";

import { IBody } from "../../core/type";

// {
//     "product": {
//         "title": "iPhone 15 pro",
//         "pertange_discount": 10,
//         "price": 1499.99,
//         "brand": "Apple",
//         "is_new": true
//     },
//     "category": {
//         "name": "Celulares",
//         "description": "Celulares de la marca apple"
//     }
// }

function mapProduct(product) {
  const productMap = {
    ...product,
    isNew: product.is_new,
    pertangeDiscount: product.pertange_discount,
  };

  delete productMap.is_new;
  delete productMap.pertange_discount;

  if (product.category_id) {
    productMap.categoryId = product.category_id;
    delete productMap.category_id;
  }

  return productMap;
}

export function mapInsertProduct(body: IBody) {
  const { product, category } = body;

  // caso 1: Que nos envien product.category_id y category
  if (product.category_id && category) {
    return response(false, "No puedes enviar un category_id y category");
  }

  // caso 2: Nos envian product y category
  if (product && category) {
    const insertData = {
      ...mapProduct(product),
      category: {
        create: {
          ...category,
        },
      },
    };

    return response(true, insertData);
  }

  // 3: Donde solo envien product
  return response(true, mapProduct(product));
}
