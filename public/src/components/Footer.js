import React from "react";
import { Link } from "react-router-dom";
import "./Footer.css";

function Footer() {
  return (
    <footer>
      <div className="Footer-Container">
        <div className="Footer">
          <div className="Footer-items">
            <div className="CONTACT">
              <a
                className="nav-links"
                href="mailto:pbn.project.de@gmail.com?body="
              >
                Contact
              </a>
            </div>
            <div className="COPYRIGHT">
              <Link to="" className="nav-links">
                © PBN-Project 2022
              </Link>
            </div>
            <div className="IMPRESSUM">
              <Link to="/home" className="nav-links">
                Legal Notice
              </Link>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
