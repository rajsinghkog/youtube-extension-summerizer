document.getElementById('getSummaryBtn').addEventListener('click', async function() {
    const summaryElement = document.getElementById('summary');


    chrome.tabs.query({ active: true, currentWindow: true }, async function(tabs) {
        const url = tabs[0].url;

       
        if (url && url.includes('youtube.com/watch?v=')) {
            try {
                const response = await fetch(`http://localhost:8000/summary?url=${encodeURIComponent(url)}`);
                if (response.ok) {
                    const data = await response.json();
                    summaryElement.innerText = data.summary;
                } else {
                    summaryElement.innerText = 'Error: Unable to fetch summary';
                }
            } catch (error) {
                summaryElement.innerText = 'Error: ' + error.message;
            }
        } else {
            summaryElement.innerText = 'This is not  valid YouTube video URL.';
        }
    });
});
