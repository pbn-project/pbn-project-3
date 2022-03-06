import React from "react";
import "../../App.css";
import "./Information.css";

export default function Information() {
  return (
    <div className="Information-Container">
      <div className="info-img">
        <img alt="paint by numbers" src="images/coco.png" />
      </div>
      <div className="text-info">
        <p>
          <p>PBN-Project</p>
          The »PBN-Project« allows users to create their own designs using
          filters programmed with Python. The aim of this project is to create a
          freely accessible and user-friendly tool that allows people without
          design knowledge to create individual designs. This is the
          Beta-Version, so we are currently working on the Alpha-Version. We
          hope you have fun using it and feel free to{" "}
          <a href="mailto:pbn.project.de@gmail.com?body=My custom mail body">
            contact us
          </a>
          !<p>This project was created as a bachelor thesis in 2022.</p>
        </p>
      </div>
      <div></div>
    </div>
  );
}
