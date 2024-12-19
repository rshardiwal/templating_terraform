import React, { useEffect, useState } from 'react';

const StreamOutput = ({ url }) => {
  const [lines, setLines] = useState([]);

  useEffect(() => {
    console.log('in side use effect');
    const eventSource = new EventSource(url);

    eventSource.onopen = () => {
      console.log('Connection to server opened.');
    };

    eventSource.onmessage = (event) => {
      console.log('New message:', event.data);
      setLines((prevLines) => [event.data, ...prevLines]); // Prepend new lines
    };

    eventSource.onerror = (err) => {
      console.error('EventSource failed:', err);
      eventSource.close();
    };

    return () => {
      eventSource.close();
    };
  }, [url]);

  return (
    <div>
      <h1>Streamed Output</h1>
      <pre>
        {lines.map((line, index) => (
          <div key={index}>{line}</div>
        ))}
      </pre>
    </div>
  );
};

export default StreamOutput;
