import { prisma } from "../../db";
import { responseError, responseSuccess } from "../../network/responses";
import { mapInsertProduct } from "./utils";

// READ

export async function list(req, res) {
  try {
    const products = await prisma.product.findMany();

    responseSuccess({ res, data: products });
  } catch (error) {
    responseError({ res, data: error.message });
  }
}

// READ by id

export async function getById(req, res) {
  try {
    const product = await prisma.product.findUnique({
      where: {
        id: Number(req.params.id),
      },
    });

    if (!product) {
      return responseError({ res, data: "Product not found" });
    }

    return responseSuccess({ res, data: product });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}

// CREATE

export async function store(req, res) {
  try {
    const { ok, data } = mapInsertProduct(req.body);

    if (!ok) {
      return responseError({ res, data });
    }

    const newProduct = await prisma.product.create({ data });

    return responseSuccess({ res, data: newProduct });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}

// export async function store(req, res) {
//   try {
//     const { product, category } = req.body;

//     const productMap = {
//       ...product,
//       isNew: product.is_new,
//       pertangeDiscount: product.pertange_discount,
//     };

//     delete productMap.is_new;
//     delete productMap.pertange_discount;

//     if (product.category_id) {
//       productMap.categoryId = product.category_id;
//       delete productMap.category_id;
//     }

//     const insertData = {
//       ...productMap,
//     };

//     const newProduct = await prisma.product.create({
//       data: {
//         ...productMap,
//         category: {
//           create: {
//             ...category,
//           },
//         },
//       },
//     });

//     return responseSuccess({ res, data: newProduct });
//   } catch (error) {
//     return responseError({ res, data: error.message });
//   }
// }
