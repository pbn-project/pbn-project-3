import React from "react";
import { Link } from "react-router-dom";

function VideoPreview(props) {
  return (
    <>
      <Link className="video-item-link" to={props.path}>
        <video className="VIDEO" src={props.src} autoPlay loop muted />
      </Link>
    </>
  );
}

export default VideoPreview;
