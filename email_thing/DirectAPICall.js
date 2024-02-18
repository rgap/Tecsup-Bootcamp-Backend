// Importing the sib-api-v3-sdk module using ES module syntax
import dotenv from "dotenv";
import SibApiV3Sdk from "sib-api-v3-sdk";
dotenv.config();

const defaultClient = SibApiV3Sdk.ApiClient.instance;

// Configure API key authorization: api-key
const apiKey = defaultClient.authentications["api-key"];
apiKey.apiKey = process.env.SMTP_PASS; // Ensure to replace YOUR_API_KEY with your actual API key

const apiInstance = new SibApiV3Sdk.TransactionalEmailsApi();

const sendSmtpEmail = {
  to: [
    {
      email: "r.guzmanap@gmail.com",
      name: "John Doe",
    },
  ],
  templateId: 59,
  params: {
    name: "John",
    surname: "Doe",
  },
  headers: {
    "X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2",
  },
};

// Sending the email
apiInstance.sendTransacEmail(sendSmtpEmail).then(
  (data) => {
    console.log("API called successfully. Returned data: " + JSON.stringify(data));
  },
  (error) => {
    console.error("Error sending the email: ", error);
  }
);
