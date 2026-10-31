(async () => {
  const blocks = document.querySelectorAll('code.language-mermaid');
  if (!blocks.length) return;
  try {
    const { default: mermaid } = await import(new URL('../vendor/mermaid.esm.min.mjs', document.currentScript.src).href);
    mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', theme: document.documentElement.classList.contains('light') ? 'neutral' : 'dark' });
    for (const block of blocks) {
      const container = document.createElement('div');
      container.className = 'mermaid';
      container.textContent = block.textContent;
      block.parentElement.replaceWith(container);
    }
    await mermaid.run({ querySelector: '.mermaid' });
  } catch (error) { console.warn('Diagram unavailable; source remains available.', error); }
})();
