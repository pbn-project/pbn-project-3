"use strict";

import React from "react";
import reactCSS from "reactcss";
import { CompactPicker } from "react-color";
import "./ColorWheel.css";

class SketchExample extends React.Component {
  state = {
    displayColorPicker: false,
    color: {
      r: "250",
      g: "40",
      b: "255",
      a: "1",
    },
  };

  handleClick = () => {
    this.setState({ displayColorPicker: !this.state.displayColorPicker });
  };

  handleClose = () => {
    this.setState({ displayColorPicker: false });
  };

  handleChange = (color) => {
    this.setState({ color: color.rgb });
  };

  render() {
    const styles = reactCSS({
      default: {
        color: {
          width: "100%",
          height: "90px",
          borderRadius: "0px",
          background: `rgba(${this.state.color.r}, ${this.state.color.g}, ${this.state.color.b}, ${this.state.color.a})`,
        },

        popover: {
          zIndex: "2",
        },
        cover: {
          position: "fixed",
          top: "70px",
          right: "0px",
          bottom: "0px",
          left: "70px",
        },
      },
    });

    return (
      <div className="color-grid">
        <div style={styles.color}>
          <CompactPicker
            color={this.state.color}
            onChange={this.handleChange}
          />
        </div>
      </div>
    );
  }
}

export default SketchExample;
