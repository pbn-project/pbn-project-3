import React, { useState, useEffect, useRef } from "react";
import "./Settingsbar.css";
import { VscSettingsGear } from "react-icons/vsc";
import { CSSTransition } from "react-transition-group";
import Form from "./Form";
import { Icon } from "./Icons";

function SettingsBar() {
  return (
    <Navbar>
      <DropdownMenu></DropdownMenu>
    </Navbar>
  );
}

function Navbar(props) {
  return (
    <nav className="navbarSettings">
      <ul className="navbarSettings-nav">{props.children}</ul>
    </nav>
  );
}

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
        className="menu-item"
        onClick={() => props.goToMenu && setActiveMenu(props.goToMenu)}
      >
        <span className="icon-button">{props.leftIcon}</span>
        {props.children}
        <span className="icon-right">{props.rightIcon}</span>
      </a>
    );
  }

  return (
    <div className="dropdown" style={{ height: menuHeight }} ref={dropdownRef}>
      <CSSTransition
        in={activeMenu === "main"}
        timeout={500}
        classNames="menu-primary"
        unmountOnExit
        onEnter={calcHeight}
      >
        <div className="menu">
          <DropdownItem
            leftIcon={<VscSettingsGear className="icon" />}
            goToMenu="settings"
          >
            <Icon></Icon>
          </DropdownItem>
        </div>
      </CSSTransition>

      <CSSTransition
        in={activeMenu === "settings"}
        timeout={500}
        classNames="menu-secondary"
        unmountOnExit
        onEnter={calcHeight}
      >
        <div className="menu">
          <DropdownItem
            goToMenu="main"
            leftIcon={<VscSettingsGear className="icon" />}
          >
            <p>Settings</p>
          </DropdownItem>

          <div className="settingsInterface">
            <Form />
          </div>
        </div>
      </CSSTransition>
    </div>
  );
}

export default SettingsBar;
