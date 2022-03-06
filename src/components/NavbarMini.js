import React, { useState } from "react";
import { Link } from "react-router-dom";

import "./NavbarMini.css";

function NavbarMini() {
  const [setClick] = useState(false);

  const closeMobileMenu = () => setClick(false);

  return (
    <>
      <nav className="navbar">
        <div className="navbar-container">
          <div>
            <Link to="/library" className="nav-links" onClick={closeMobileMenu}>
              Library
            </Link>
          </div>

          <div>
            <Link
              to="/instruction"
              className="nav-links"
              onClick={closeMobileMenu}
            >
              Instructions
            </Link>
          </div>

          <div>
            <Link
              to="/information"
              className="nav-links"
              onClick={closeMobileMenu}
            >
              Information
            </Link>
          </div>
        </div>
      </nav>
    </>
  );
}

export default NavbarMini;
