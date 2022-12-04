import React, { useState } from 'react';
import Button from './Button';
import SelectBox from './SelectBox';
import TextBox from './TextBox';
import './styles/style.scss';
import { postGenerateTextEndpoint } from '../utils';

function Prediction() {
  const [text, setText] = useState("");
  const [model, setModel] = useState('thutmose');
  const [generatedText, postGenerateText] = postGenerateTextEndpoint();

  const generateText = () => {
    postGenerateText({ text, model, userId: 1 });
  }

  return (
    <div className='app-container'>
      <form noValidate autoComplete='off'>
        <h1>Inverted Text Normalization</h1>
        <SelectBox model={model} setModel={setModel} />
        <TextBox text={text} setText={setText} />
        <Button onClick={generateText} />
      </form>

      {generatedText.pending &&
        <div className='result pending'>Please wait</div>}

      {generatedText.complete &&
        (generatedText.error ?
          <div className='result error'>Bad Request</div> :
          <div className='result valid'>
            {generatedText.data.inverted_text}
          </div>)}
    </div>
  );
}

export default Prediction;
