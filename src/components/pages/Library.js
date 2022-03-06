import React from "react";
import "../../App.css";
import "./Library.css";
import { Link } from "react-router-dom";

function Library() {
  return (
    <>
      <div className="library-container1">
        <div className="filter-div">
          <Link to="/project">
            <img alt="hey" src="images/hey.gif"></img>
          </Link>
        </div>

        <div className="filter-div">
          <div className="locked">
            <p>This filter is locked.</p>
          </div>

          <img alt="locked filter" src="images/02-FILTER.png"></img>
        </div>

        <div className="filter-div">
          <div className="locked">
            <p>This filter is locked.</p>
          </div>

          <img alt="locked filter" src="images/02-FILTER.png"></img>
        </div>

        <div className="filter-div">
          <div className="locked">
            <p>This filter is locked.</p>
          </div>

          <img alt="locked filter" src="images/02-FILTER.png"></img>
        </div>

        <div className="filter-div">
          <div className="locked">
            <p>This filter is locked.</p>
          </div>

          <img alt="locked filter" src="images/02-FILTER.png"></img>
        </div>

        <div className="filter-div">
          <div className="locked">
            <p>This filter is locked.</p>
          </div>

          <img alt="locked filter" src="images/02-FILTER.png"></img>
        </div>
      </div>
    </>
  );
}

export default Library;
