import { useState } from "react";
import APIService from "./APIService";
import axios from "axios";

const TestForm = (props) => {
  const [title, setTitle] = useState("");
  const [fontSize, setFontSize] = useState("");

  async function insertData() {
    const response = await axios.post("/test_0", { title, fontSize });
    console.log(response);
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    insertData();
    setTitle("");
    setFontSize("");
  };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label htmlFor="title">Title</label>
        <input
          type="text"
          placeholder="Enter title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />

        <label htmlFor="fontSize">Font Size</label>
        <textarea
          placeholder="30pt"
          type="number"
          rows="6"
          value={fontSize}
          onChange={(e) => setFontSize(e.target.value)}
          required
        ></textarea>

        <button>Sent Data to flask</button>
      </form>
    </div>
  );
};

export default TestForm;
