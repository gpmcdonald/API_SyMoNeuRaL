document.addEventListener('DOMContentLoaded', () => {
    const sendBtn = document.getElementById('send');
    const input = document.getElementById('message');
    const consoleEl = document.getElementById('console');

    sendBtn.addEventListener('click', () => {
        const msg = input.value.trim();
        if(msg) {
            const p = document.createElement('p');
            p.textContent = `You: ${msg}`;
            consoleEl.appendChild(p);
            input.value = '';
        }
    });
});