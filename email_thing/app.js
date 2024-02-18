import dotenv from "dotenv";
import nodemailer from "nodemailer";
dotenv.config();

async function sendEmail() {
  // Create a transporter
  let transporter = nodemailer.createTransport({
    host: "smtp-relay.sendinblue.com", // SMTP server host
    port: 587, // SMTP server port
    auth: {
      user: "r.guzmanap@gmail.com", // Replace with your email
      pass: process.env.SMTP_PASS,
    },
  });

  //   xsmtpsib-fc1c2fdab0553245a4d940c17834379e00d370e9226fae659c6371ed56ab24b2-bRONAXD8MP5vjf2C

  // Set up email data
  let mailOptions = {
    from: "r.guzmanap@gmail.com", // Replace with your email
    to: "rgap449@gmail.com", // Replace with recipient's email
    subject: "Hello ✔", // Subject line
    text: "Hello world?", // Plain text body
    html: "<b>Hello world?</b>", // HTML body
  };

  // Send email
  try {
    let info = await transporter.sendMail(mailOptions);
    console.log("Message sent: %s", info.messageId);
  } catch (error) {
    console.error("Error sending email: ", error);
  }
}

sendEmail();
