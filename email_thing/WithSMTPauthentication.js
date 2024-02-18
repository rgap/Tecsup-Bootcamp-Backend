import dotenv from "dotenv";
import nodemailer from "nodemailer";
dotenv.config();

async function sendEmail() {
  // Create a transporter
  let transporter = nodemailer.createTransport({
    host: "smtp-relay.brevo.com", // SMTP server host
    port: 587, // SMTP server port
    auth: {
      user: "r.guzmanap@gmail.com", // Replace with your email
      pass: process.env.SMTP_PASS,
    },
  });

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
