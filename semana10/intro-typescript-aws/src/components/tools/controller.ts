import type { Request, Response } from "express";
import type { FileArray, UploadedFile } from "express-fileupload";
import { responseError, responseSuccess } from "../../network/responses";
import { uploadFile } from "../../services/aws";
import { handleResponseError } from "../../utils";

export async function storeFile(req: Request, res: Response) {
  try {
    if (!req.files) {
      return responseError({
        res,
        data: "Not files found.",
        status: 400,
      });
    }

    const { file } = req.files as FileArray;
    console.log(file);

    const { location, data } = await uploadFile(file as UploadedFile);

    return responseSuccess({
      res,
      data: {
        location,
        data,
      },
    });
  } catch (error) {
    return handleResponseError(res, error);
  }
}
