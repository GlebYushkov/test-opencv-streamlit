import cv2
import streamlit as st
from streamlit_webrtc import VideoProcessorBase, webrtc_streamer

st.write('HELLO WORLD')
webrtc_streamer(key="example")
