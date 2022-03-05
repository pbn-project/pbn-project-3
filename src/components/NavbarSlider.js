import React, { useState, useEffect, useRef } from "react";
import "./NavbarSlider.css";
import { VscSettingsGear } from "react-icons/vsc";
import { CSSTransition } from "react-transition-group";
import Logo from "./Logo";

import NavbarMini from "./NavbarMini";

function NavbarSlider() {
  return (
    <Navbar className="Navbar-Menu">
      <DropdownMenu></DropdownMenu>
    </Navbar>
  );
}

function Navbar(props) {
  return (
    <nav className="navbarslider">
      <ul className="navbarslider-nav">{props.children}</ul>
    </nav>
  );
}

/* function NavItem(props) {
  const [open, setOpen] = useState(false);

  return (
    <li className="navslider-item">
      <a href="#" className="icon-button" onClick={() => setOpen(!open)}>
        {props.icon}
      </a>

      {open && props.children}
    </li>
  );
} */

function DropdownMenu() {
  const [activeMenu, setActiveMenu] = useState("main");
  const [menuHeight, setMenuHeight] = useState(null);
  const dropdownRef = useRef(null);

  useEffect(() => {
    setMenuHeight(dropdownRef.current?.firstChild.offsetHeight);
  }, []);

  function calcHeight(el) {
    const height = el.offsetHeight;
    setMenuHeight(height);
  }

  function DropdownItem(props) {
    return (
      <a
        href="#"
        className="NavbarMenu-item"
        onClick={() => props.goToMenu && setActiveMenu(props.goToMenu)}
      >
        <span></span>
        {props.children}
        <span></span>
      </a>
    );
  }

  return (
    <>
      <div
        className="dropdownMenu"
        style={{ height: menuHeight }}
        ref={dropdownRef}
      >
        <Logo />
        <CSSTransition
          in={activeMenu === "main"}
          timeout={500}
          classNames="NavbarMenu-primary"
          unmountOnExit
          onEnter={calcHeight}
        >
          <div className="NavbarMenu">
            <DropdownItem className="MENU" goToMenu="settings">
              <p>Menu</p>
            </DropdownItem>
          </div>
        </CSSTransition>

        <CSSTransition
          in={activeMenu === "settings"}
          timeout={500}
          classNames="NavbarMenu-secondary"
          unmountOnExit
          onEnter={calcHeight}
        >
          <div className="NavbarMenu">
            <DropdownItem
              goToMenu="main"
              leftIcon={<VscSettingsGear className="icon" />}
            >
              <p>Close</p>
            </DropdownItem>

            <div className="Interface">
              <NavbarMini></NavbarMini>
            </div>
          </div>
        </CSSTransition>
      </div>
    </>
  );
}

export default NavbarSlider;
