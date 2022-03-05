import React, { useRef, useState, useEffect } from "react";
import emailjs from "@emailjs/browser";

export const ContactUs = () => {
  const [block, setBlock] = useState([{}]);

  useEffect(() => {
    fetch("/test_3")
      .then((res) => res.json())
      .then((data) => {
        setBlock(data);
        console.log(data);
      });
  }, []);

  const form = useRef();

  const sendEmail = (e) => {
    e.preventDefault();

    emailjs
      .sendForm("gmail", "template_dvcfnti", form.current, "oidbM5BXKLjuAtDTB")
      .then(
        (result) => {
          console.log(result.text);
        },
        (error) => {
          console.log(error.text);
        }
      );
  };

  return (
    <form ref={form} onSubmit={sendEmail}>
      <label>Name</label>
      <input type="text" name="user_name" />
      <label>Email</label>
      <input type="email" name="user_email" />
      <label>Message</label>
      <textarea name="message" />
      <div name="div">hallo</div>
      <img name="img2" src="images/hey.gif"></img>
      <img
        src={`data:image/gif;base64,${block.image_string}`}
        alt="Loading"
        name="img"
      />
      <input type="submit" value="Send" />
    </form>
  );
};
