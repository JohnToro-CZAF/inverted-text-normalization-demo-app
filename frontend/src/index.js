import React from "react";
import { render } from 'react-dom';

import Prediction from "./components/Prediction";  // new

function App() {
  return (
    <Prediction />
  )
}

const rootElement = document.getElementById("root")
render(<App />, rootElement)