import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { UploadedFile } from "express-fileupload";

const s3Client = new S3Client({
  region: "us-west-2",
  credentials: {
    accessKeyId: process.env.AWS_ACCESS_KEY_ID as string,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY as string,
  },
});

export async function uploadFile(file: UploadedFile) {
  const keyFile = `images/codigo-15-${Date.now()}-${file.name}`;
  const params = {
    Bucket: "test-2024-rgap-node-ts",
    Key: keyFile,
    Body: file.data,
  };

  const data = await s3Client.send(new PutObjectCommand(params));

  return {
    location: keyFile,
    data,
  };
}
