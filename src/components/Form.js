import React, { useEffect, useState } from "react";

import "./Form.css";
import SketchExample from "./SettingsProject/ColorWheel";
import { saveAs } from "file-saver";
import axios from "axios";
import Splitfilter from "./Splitfilter";

const Form = (props) => {
  const [navbarOpen, setNavbarOpen] = useState(false);
  const handleToggle = () => {
    setNavbarOpen(!navbarOpen);
  };
  const closeMenu = () => {
    setNavbarOpen(false);
  };

  const [block, setBlock] = useState([{}]);
  useEffect(() => {
    fetch("/test_3")
      .then((res) => res.json())
      .then((data) => {
        setBlock(data);
      });
  }, []);

  const downloadImage = () => {
    saveAs(`data:image/gif;base64,${block.image_string}`); // Put your image url here.
  };

  const [visible, setVisible] = React.useState(false);

  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [frames, setFrames] = useState("");
  const [formatX, setFormatX] = useState("");
  const [formatY, setFormatY] = useState("");
  const [fontSize, setFontSize] = useState("");
  const [splitOptionYes, setSplitOptionYes] = useState("false");
  const [splitOptionNo, setSplitOptionNo] = useState("false");
  const [splitDistance, setSplitDistance] = useState("");

  const [colorBGR, setColorBGR] = useState("");
  const [colorBGG, setColorBGG] = useState("");
  const [colorBGB, setColorBGB] = useState("");

  const [color1R, setColor1R] = useState("");
  const [color1G, setColor1G] = useState("");
  const [color1B, setColor1B] = useState("");

  const [color2R, setColor2R] = useState("");
  const [color2G, setColor2G] = useState("");
  const [color2B, setColor2B] = useState("");

  const [color3R, setColor3R] = useState("");
  const [color3G, setColor3G] = useState("");
  const [color3B, setColor3B] = useState("");

  const [color4R, setColor4R] = useState("");
  const [color4G, setColor4G] = useState("");
  const [color4B, setColor4B] = useState("");

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
      <nav className="navBar">
        <button className="form-button" onClick={handleToggle}>
          {navbarOpen ? "Close" : "Form"}
        </button>

        <form
          onSubmit={handleSubmit}
          className="form-box"
          className={`form-box ${navbarOpen ? " showMenu" : ""}`}
        >
          <label htmlFor="title" className="form-label">
            Text
          </label>
          <input
            type="text"
            className="form-control"
            placeholder="Write Text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />

          <label htmlFor="body" className="form-label">
            Format
          </label>
          <div className="double-box">
            <input
              className="form-control"
              placeholder="1400px"
              rows="6"
              value={formatX}
              onChange={(e) => setFormatX(e.target.value)}
            ></input>
            <input
              className="form-control"
              placeholder="1000px"
              rows="6"
              value={formatY}
              onChange={(e) => setFormatY(e.target.value)}
            ></input>
          </div>
          <label className="form-label">Frames</label>
          <input
            type="text"
            className="form-control"
            placeholder="25"
            value={frames}
            onChange={(e) => setFrames(e.target.value)}
          />
          <label className="form-label">Font Size</label>
          <input
            type="text"
            className="form-control"
            placeholder="250pt"
            value={fontSize}
            onChange={(e) => setFontSize(e.target.value)}
          />
          <label className="form-label">Should they split?</label>

          <div className="split-option">
            <button
              className="form-control-button"
              value={splitOptionYes}
              onClick={() => setSplitOptionYes(true)}
            >
              Yes
            </button>
            <button
              className="form-control-button"
              placeholder="No"
              value={splitOptionNo}
              onClick={() => setSplitOptionNo(true)}
            >
              No
            </button>
          </div>
          <label className="form-label">Split distance</label>
          <input
            type="text"
            className="form-control"
            placeholder="40"
            value={splitDistance}
            onChange={(e) => setSplitDistance(e.target.value)}
          />
          <label className="form-label-rgb">Read RGB </label>
          <div className="color">
            <SketchExample />
          </div>

          <label className="form-label-rgb">Background Color</label>
          <div className="color-rgb">
            <input
              type="text"
              className="form-control"
              placeholder="R"
              value={colorBGR}
              onChange={(e) => setColorBGR(e.target.value)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="G"
              value={colorBGG}
              onChange={(e) => setColorBGG(e.target.value)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="B"
              value={colorBGB}
              onChange={(e) => setColorBGB(e.target.value)}
            />
          </div>

          <label className="form-label-rgb">Color ONE</label>
          <div className="color-rgb">
            <input
              type="text"
              className="form-control"
              placeholder="R"
              value={color1R}
              onChange={(e) => setColor1R(e.target.value)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="G"
              value={color1G}
              onChange={(e) => setColor1G(e.target.value)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="B"
              value={color1B}
              onChange={(e) => setColor1B(e.target.value)}
            />
          </div>
          <label className="form-label-rgb">Color Two</label>
          <div className="color-rgb">
            <input
              type="text"
              className="form-control"
              placeholder="R"
              value={color2R}
              onChange={(e) => setColor2R(e.target.value)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="G"
              value={color2G}
              onChange={(e) => setColor2G(e.target.value)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="B"
              value={color2B}
              onChange={(e) => setColor2B(e.target.value)}
            />
          </div>

          <label className="form-label-rgb">Color Two</label>
          <div className="color-rgb">
            <input
              type="text"
              className="form-control"
              placeholder="R"
              value={color3R}
              onChange={(e) => setColor3R(e.target.value)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="G"
              value={color3G}
              onChange={(e) => setColor3G(e.target.value)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="B"
              value={color3B}
              onChange={(e) => setColor3B(e.target.value)}
            />
          </div>

          <label className="form-label-rgb">Color Four</label>
          <div className="color-rgb">
            <input
              type="text"
              className="form-control"
              placeholder="R"
              value={color4R}
              onChange={(e) => setColor4R(e.target.value)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="G"
              value={color4G}
              onChange={(e) => setColor4G(e.target.value)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="B"
              value={color4B}
              onChange={(e) => setColor4B(e.target.value)}
            />
          </div>
          <button
            className="publish-button"
            onClick={() => {
              closeMenu();
              setVisible(true);
            }}
            exact
          >
            Sent Data
          </button>
          <button className="dowload-button" onClick={downloadImage}>
            Download
          </button>
        </form>
      </nav>
      {visible && (
        <div className="splitfilter">
          <Splitfilter />
        </div>
      )}
    </div>
  );
};

export default Form;
