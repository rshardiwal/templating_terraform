import React from 'react';
import { createRoot } from 'react-dom/client';
import StreamOutput from './components/StreamOutput';

const streamUrl = 'http://127.0.0.1:5000/stream_output'; // Replace with your actual URL

const container = document.getElementById('root');
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <StreamOutput url={streamUrl} />
  </React.StrictMode>
);
