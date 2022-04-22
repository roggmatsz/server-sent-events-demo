const eventSources = [];
function startEventSource(i) {
   if (eventSources[i] !== undefined) return;

   const eventSource = eventSources[i] = new EventSource('http://localhost/sse' + i);
   eventSource.onopen = event => console.log('Source open');
   eventSource.onerror = error => console.warn('Event Source error', error);
   eventSource.onmessage = event => console.log(event.data);
}

function closeEventSource(i) {
   if (eventSources[i] === undefined) return;

   console.log('Closing Event Source');
   eventSources[i].close();
   delete eventSources[i];
}