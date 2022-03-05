import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Home from "./components/pages/Home";
import NavbarSlider from "./components/NavbarSlider";
import Library from "./components/pages/Library";
import Instruction from "./components/pages/Instrustion";
import Information from "./components/pages/Information";
import Footer from "./components/Footer";
import ProjectPreview from "./components/SettingsProject/ProjectPreview";
// import TestForm from "./components/TestForm";

function App() {
  /*   const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("/test_0")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []); */
  return (
    <>
      {/* <TestForm></TestForm> */}
      <div>
        {/*  {typeof data.message === "undefined" ? (
          <p>Loading...</p>
        ) : (
          data.message.map((message, i) => <p key={i}>{message}</p>)
        )} */}
      </div>
      <Router>
        <NavbarSlider className="navi" />
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/project" element={<ProjectPreview />} />
          <Route exact path="/home" element={<Home />} />
          <Route exact path="/library" element={<Library />} />
          <Route exact path="/instruction" element={<Instruction />} />
          <Route exact path="/information" element={<Information />} />
        </Routes>
        <Footer />
      </Router>
    </>
  );
}

export default App;
