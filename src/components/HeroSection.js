import React from "react";
import "../App.css";
import "./HeroSection.css";
import VideoPreview from "./VideoPreview";

function HeroSection() {
  return (
    <div className="hero-container">
      <div className="video-1">
        <div className="videos">
          <VideoPreview src="videos/FILTER_1_Splittype_2.mp4" path="/project" />
        </div>
        <div className="imgMiddle">
          <VideoPreview src="videos/PreviewMiddle.mp4" path="/project" />
        </div>

        <div className="imgMini">
          <VideoPreview src="videos/PreviewMini.mp4" path="/project" />
        </div>
      </div>
    </div>
  );
}
export default HeroSection;
